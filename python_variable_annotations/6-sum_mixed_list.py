#!/usr/bin/env python3
"""Variable Annotations"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list float or int number"""
    suma: float = 0
    for num in mxd_lst:
        suma = suma + num
    return suma
