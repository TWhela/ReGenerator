"""Post-blend face customisation layers."""

import random

from . import data
from .sampling import constrained_float

SKIN_LAYERS = [
    "Dermaesthetic", "ComplexionMask1", "Complexion1", "Complexion2",
    "ComplexionMask2", "Scars", "Accents1", "Accents2",
    "ColorlessAccents1", "ColorlessAccents2",
]
PAINT_LAYERS = ["TattooMask", "MakeupFullPaintMask1", "MakeupFullPaintMask2"]
MAKEUP_LAYERS = [
    "Cheeks1", "Cheeks2", "Lipstick1", "Lipstick2",
    "Eyeshadow1", "Eyeshadow2", "Eyeliner1", "Eyeliner2",
]

CHANCE_OF_PAINT = 0.05
CHANCE_OF_MAKEUP_FEMALE = 0.25
CHANCE_OF_MAKEUP_MALE = 0.1


def _build_layer(name):
    options = data.layer_options[name]
    colours = options["Col"]
    return {
        "Intensity": constrained_float(0.0, 0.8, 0.4, 0.2),
        "ModulationValue": {"Value": random.choice(colours) if colours else ""},
        "Name": name,
        "Value": {"Value": random.choice(options["Sub"])},
    }


def _pick(pool, minimum, maximum):
    return [_build_layer(name) for name in random.sample(pool, k=random.randint(minimum, maximum))]


def _makeup_chance(sex):
    return CHANCE_OF_MAKEUP_FEMALE if sex == "Female" else CHANCE_OF_MAKEUP_MALE


def build_customisation_layers(sex):
    layers = _pick(SKIN_LAYERS, 2, 8)

    if random.random() < CHANCE_OF_PAINT:
        layers += _pick(PAINT_LAYERS, 1, 2)

    if random.random() < _makeup_chance(sex):
        layers += _pick(MAKEUP_LAYERS, 1, 2)

    return layers
