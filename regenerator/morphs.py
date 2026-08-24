"""Facial morph sliders and bone region data."""

import random

from . import data
from .sampling import constrained_float

HEAD_SHAPE_REGION = {"Male": 50, "Female": 23}


def _tables(sex):
    if sex == "Male":
        return data.region_data_male, data.sculpt_data_male, data.sculpt_list_male
    if sex == "Female":
        return data.region_data_female, data.sculpt_data_female, data.sculpt_list_female
    raise ValueError(f"Unknown sex: {sex!r}")


def build_morph_sliders(sex, primary, secondary):
    """Blend the primary and secondary ethnicity morph for each facial feature."""
    morphs = []

    for feature in data.features:
        primary_morph = f"{sex.lower()}_{primary}_{feature}"
        secondary_morph = f"{sex.lower()}_{secondary}_{feature}"
        value = constrained_float(0.0, 1.0, 1.0, 0.25)

        leading, trailing = primary_morph, secondary_morph
        if random.random() <= 0.3:
            leading, trailing = trailing, leading

        morphs.append({"Name": leading, "Value": value})
        morphs.append({"Name": trailing, "Value": 1.0 - value})

    return morphs


def _ethnicity_regions(region_data, primary, secondary):
    primary_sliders = []
    secondary_sliders = []

    for feature in data.features:
        value = constrained_float(0.0, 1.0, 0.75, 0.25)
        primary_sliders.append({"GroupName": feature, "ID": 0, "Value": value})
        secondary_sliders.append({"GroupName": feature, "ID": 0, "Value": 1.0 - value})

    return [
        {"RegionID": region_data[primary], "SlidersA": primary_sliders},
        {"RegionID": region_data[secondary], "SlidersA": secondary_sliders},
    ]


def _sculpt_regions(sex, sculpt_data, sculpt_list):
    regions = []

    for sculpt in sculpt_list:
        sliders = []
        for group in sculpt_data[sculpt]:
            if sculpt == HEAD_SHAPE_REGION[sex]:
                value = constrained_float(0.0, 1.0, 0.25, 0.1)
            else:
                value = constrained_float(-1.0, 1.0, 0.0, 0.5)
            sliders.append({"GroupName": "", "ID": group, "Value": value})

        regions.append({"RegionID": sculpt, "SlidersA": sliders})

    return regions


def build_morph_regions(sex, primary, secondary):
    region_data, sculpt_data, sculpt_list = _tables(sex)
    return (
        _ethnicity_regions(region_data, primary, secondary)
        + _sculpt_regions(sex, sculpt_data, sculpt_list)
    )
