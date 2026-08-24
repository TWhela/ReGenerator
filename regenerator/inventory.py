import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from . import data

MORPH_NAME = re.compile(r"^(?:male|female)_(af|as|eu)_(yo1|md1|md2|ol1)_", re.IGNORECASE)

ETHNICITY_LABELS = {"af": "African", "as": "Asian", "eu": "European"}
AGE_LABELS = {"yo1": "Young", "md1": "Middle", "md2": "Middle", "ol1": "Old"}

SKIN_TONE_ETHNICITY = {
    tone: ethnicity
    for ethnicity, tones in data.skin_color_options.items()
    for tone in tones
}

REGION_ETHNICITY = {
    sex: {region: key.split("_")[0] for key, region in table.items()}
    for sex, table in (("Male", data.region_data_male), ("Female", data.region_data_female))
}


@dataclass
class Preset:
    path: Path
    sex: str = None
    ethnicity: str = None
    age: str = None

    @property
    def is_recognised(self):
        return self.ethnicity is not None


def _morph_weights(sliders):
    weights = Counter()
    for slider in sliders:
        match = MORPH_NAME.match(str(slider.get("Name", "")))
        if match:
            weights[(match.group(1).lower(), match.group(2).lower())] += float(
                slider.get("Value", 0.0)
            )
    return weights


def _ethnicity_from_regions(regions, sex):
    """The generator writes the primary ethnicity's bone region first."""
    lookup = REGION_ETHNICITY.get(sex, {})
    for region in regions:
        ethnicity = lookup.get(region.get("RegionID"))
        if ethnicity:
            return ethnicity
    return None


def read_preset(path):
    """Describe one .npc file. Unreadable or unrecognised files come back unclassified."""
    path = Path(path)
    try:
        with path.open(encoding="utf-8") as handle:
            npc = json.load(handle)
    except (OSError, ValueError):
        return Preset(path)

    if not isinstance(npc, dict):
        return Preset(path)

    sex = npc.get("Sex") if npc.get("Sex") in ("Male", "Female") else None
    weights = _morph_weights(npc.get("FacialMorphSliderDataA") or [])

    ethnicity = SKIN_TONE_ETHNICITY.get(npc.get("SkinTone"))
    if ethnicity is None:
        ethnicity = _ethnicity_from_regions(npc.get("FacialBoneRegionDataA") or [], sex)
    if ethnicity is None and weights:
        ethnicity = weights.most_common(1)[0][0][0]

    age = None
    if weights:
        matching = {key: value for key, value in weights.items() if key[0] == ethnicity}
        age = max(matching or weights, key=(matching or weights).get)[1]

    return Preset(path, sex=sex, ethnicity=ethnicity, age=age)


def scan(directory):
    """Read every .npc in a folder, sorted by name. Missing folder gives an empty list."""
    directory = Path(directory)
    if not directory.is_dir():
        return []
    return [read_preset(path) for path in sorted(directory.glob("*.npc"))]


def tally(presets):
    """Count presets by ethnicity and sex, as {ethnicity: {"Male": n, "Female": n}}."""
    counts = {key: {"Male": 0, "Female": 0} for key in ETHNICITY_LABELS}

    for preset in presets:
        if preset.is_recognised and preset.sex in ("Male", "Female"):
            counts[preset.ethnicity][preset.sex] += 1

    return counts
