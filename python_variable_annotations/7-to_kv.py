#!/usr/bin/env python
"""Variable Annotations"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple whit a string and float"""
    return k, float(v*v)
