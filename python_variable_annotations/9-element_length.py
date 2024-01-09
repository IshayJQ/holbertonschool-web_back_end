#!/usr/bin/env python3
"""Variable Annotations"""
from typing import List, Tuple, Sequence


def element_length(lst: List[str]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where the first element is a string
    and the second element is an integer.
    """
    return [(i, len(i)) for i in lst]
