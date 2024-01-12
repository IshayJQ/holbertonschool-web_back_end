#!/usr/bin/env python3
"""Size containing a start index and an end index"""
from typing import Tuple, List
import csv


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the paginated list of rows from the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        paginated_data = self.dataset()
        pages = paginated_data[start:end]

        return pages
