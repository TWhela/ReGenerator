"""Head parts and colour selection."""

import random

from . import data

EYE_CONDITIONS = ["Jaundice", "Bloodshot"]
DIRTY_TEETH = ["Teeth_Dirty", "Teeth_Dead", "Teeth_Blackened"]

CHANCE_OF_BEARD = 0.25
CHANCE_OF_JEWELRY = 0.25
CHANCE_OF_EYE_CONDITION = 0.2
CHANCE_OF_DIRTY_TEETH = 0.1


def _hair_styles(sex, androgynous):
    if androgynous:
        return data.hair_all
    return data.hair_male if sex == "Male" else data.hair_female


def _eye(prefix, side):
    if random.random() > CHANCE_OF_EYE_CONDITION:
        return f"{prefix}_{side}Eye"
    return f"{prefix}_{side}Eye_{random.choice(EYE_CONDITIONS)}"


def pick_hair_colour(primary_ethnicity, androgynous):
    if androgynous:
        return random.choice(data.hair_colors_all)
    if primary_ethnicity == "eu":
        return random.choice(data.hair_colors_natural)
    return random.choice(data.hair_colors_non_eu)


def pick_teeth():
    if random.random() > CHANCE_OF_DIRTY_TEETH:
        return "Teeth_Clean"
    return random.choice(DIRTY_TEETH)


def build_head_parts(sex, androgynous):
    """Build the fixed-order UniqueHeadPartsA slot list the Creation Kit expects.

    The empty strings are slots this generator leaves untouched; their positions
    are significant, so the list is written out in full rather than filtered.
    """
    prefix = f"Human_{sex}"

    hair = f"{prefix}_Hair_{random.choice(_hair_styles(sex, androgynous))}"
    eyebrow = f"{prefix}_Eyebrow_{random.choice(data.eyebrow_options)}"

    beard = "none"
    if sex == "Male" and random.random() < CHANCE_OF_BEARD:
        beard = f"{prefix}_Beard_{random.choice(data.beard_options)}"

    jewelry = "none"
    if sex == "Female" and random.random() < CHANCE_OF_JEWELRY:
        jewelry = f"{prefix}_Jewelry_{random.choice(data.jewelry_options)}_{sex[0]}"

    eyelashes = random.choice(["01", "02"])

    return [
        "",
        f"{prefix}_Head",
        _eye(prefix, "Right"),
        hair,
        beard,
        "",
        eyebrow,
        jewelry,
        "",
        f"{prefix}_Teeth",
        "",
        "",
        _eye(prefix, "Left"),
        f"{prefix}_Eyelashes_{eyelashes}_Top",
    ]
