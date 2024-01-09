#!/usr/bin/env python3
"""Variable Annotations"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Return a list of tuples where the first element is a string
    and the second element is an integer.
    """
    return [(i, len(i)) for i in lst]
