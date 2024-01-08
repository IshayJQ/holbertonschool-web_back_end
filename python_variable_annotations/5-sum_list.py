#!/usr/bin/env python
"""Variable Annotations"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list float number"""
    suma: float = 0
    for num in input_list:
        suma = suma + num
    return suma
