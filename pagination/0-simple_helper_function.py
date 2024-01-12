#!/usr/bin/env python3
"""Size containing a start index and an end index"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    Returns a tuple containing the start and
    end indices for the specified page.
    """
    if page < 1 or page_size < 1:
        raise ValueError("must begreater than or equal to 1.")
    start_index = (page-1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
