#!/usr/bin/env python3
"""Size containing a start index and an end index"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    Calculate the start and end indices for pagination.

    Parameters:
    - page (int): The current page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start and end indices for the specified page.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Both page and page_size must be greater than or equal to 1.")

    start_index = (page-1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
