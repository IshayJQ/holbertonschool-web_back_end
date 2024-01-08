#!/usr/bin/env python3
"""Variable Annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier
    """

    def multiplerFunction(value: float) -> float:
        """
        Return the multiplier value
        """
        return value * multiplier

    return multiplerFunction
