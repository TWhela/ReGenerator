"""Builds a complete Starfield .npc preset."""

import json
import random
import re
from dataclasses import dataclass
from pathlib import Path

from . import appearance, data, layers, morphs
from .sampling import constrained_float

SEXES = ["Male", "Female"]
SEX_FILE_CODE = {"Male": "M", "Female": "F"}
PRESET_PATTERN = re.compile(r"^ReGeneration_(?:M|F)_(\d+)\.npc$")

# Starfield ships no eu_md1 morph set; the middle-aged European assets are named md2.
AGE_KEY_OVERRIDES = {"eu_md1": "eu_md2"}


def morph_key(ethnicity, age):
    key = f"{ethnicity}_{age}"
    return AGE_KEY_OVERRIDES.get(key, key)


@dataclass
class NpcRequest:
    """What to generate. Any field left as None is chosen at random.

    Pinning `primary_ethnicity` lets a caller generate an even spread across races
    rather than relying on chance.
    """

    sex: str = None
    primary_ethnicity: str = None
    secondary_ethnicity: str = None
    age: str = None
    androgynous: bool = False

    def resolve(self):
        """Return a copy with every unset field filled in."""
        sex = self.sex or random.choice(SEXES)
        age = self.age or random.choice(data.ages)

        primary = self.primary_ethnicity
        secondary = self.secondary_ethnicity
        if primary is None and secondary is None:
            primary, secondary = random.sample(data.ethnicities, 2)
        elif secondary is None:
            secondary = random.choice([e for e in data.ethnicities if e != primary])
        elif primary is None:
            primary = random.choice([e for e in data.ethnicities if e != secondary])

        return NpcRequest(sex, primary, secondary, age, self.androgynous)

    def validate(self):
        if self.sex not in SEXES:
            raise ValueError(f"sex must be one of {SEXES}, got {self.sex!r}")
        for name, value in (("primary", self.primary_ethnicity),
                            ("secondary", self.secondary_ethnicity)):
            if value not in data.ethnicities:
                raise ValueError(
                    f"{name} ethnicity must be one of {data.ethnicities}, got {value!r}"
                )
        if self.age not in data.ages:
            raise ValueError(f"age must be one of {data.ages}, got {self.age!r}")
        if self.primary_ethnicity == self.secondary_ethnicity:
            raise ValueError(
                "primary and secondary ethnicity must differ: blending an ethnicity with "
                "itself emits a duplicate RegionID and paired morphs at 1.0 and 0.0"
            )


def generate_npc(request=None):
    request = (request or NpcRequest()).resolve()
    request.validate()

    sex = request.sex
    primary = morph_key(request.primary_ethnicity, request.age)
    secondary = morph_key(request.secondary_ethnicity, request.age)

    hair_colour = appearance.pick_hair_colour(request.primary_ethnicity, request.androgynous)

    return {
        "RaceFormID": "HumanRace",
        "SkinTone": random.choice(data.skin_color_options[request.primary_ethnicity]),
        "Sex": sex,
        "HairColor": hair_colour,
        "EyeColor": random.choice(data.eye_colors_all),
        "BrowHairColor": hair_colour,
        "FacialHairColor": hair_colour if sex == "Male" else "",
        "JewelryColor": random.choice(data.jewelry_colors),
        "TeethCustomization": appearance.pick_teeth(),
        "FacialBoneRegionDataA": morphs.build_morph_regions(sex, primary, secondary),
        "FacialMorphSliderDataA": morphs.build_morph_sliders(sex, primary, secondary),
        "MorphWeights": {
            "x": constrained_float(0.0, 1.0, 0.5, 0.25),
            "y": constrained_float(0.0, 1.0, 0.5, 0.25),
            "z": constrained_float(0.1, 0.9, 0.0, 0.2),
        },
        "PostBlendFaceCustomization": {
            "LayersA": layers.build_customisation_layers(sex)
        },
        "UniqueHeadPartsA": appearance.build_head_parts(sex, request.androgynous),
        "MiscHeadPartsA": [],
    }


def write_npc(npc, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(npc, handle, indent=3)
    return path


def preset_filename(sex, index):
    return f"ReGeneration_{SEX_FILE_CODE[sex]}_{index}.npc"


def next_preset_index(output_dir, sex):
    """Return the first index that would not overwrite an existing preset.

    Numbering continues past the highest index already present rather than
    filling gaps, so a preset deleted on purpose is not silently recreated.
    """
    directory = Path(output_dir)
    if not directory.is_dir():
        return 1

    prefix = f"ReGeneration_{SEX_FILE_CODE[sex]}_"
    used = [
        int(match.group(1))
        for path in directory.glob(f"{prefix}*.npc")
        if (match := PRESET_PATTERN.match(path.name))
    ]
    return max(used, default=0) + 1
