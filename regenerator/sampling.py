"""Random helpers shared by the morph and layer builders."""

import random


def constrained_float(minimum, maximum, mean, deviation):
    """Draw from a Gaussian distribution and clamp the result to the given range."""
    return max(minimum, min(random.gauss(mean, deviation), maximum))
