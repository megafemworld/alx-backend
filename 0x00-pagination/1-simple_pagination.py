#!/usr/bin/env python3
from typing import Tuple
"""
    The function should return a tuple of size two
    containing a start index and an end index corresponding
    to the range of indexes to return in a list
    for those particular pagination parameters.
"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """index_range that takes two integer arguments page and page_size"""
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get numbers of pages"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        i, j = index_range(page, page_size)
        data_set = self.dataset()
        if i >= len(data_set) or j >= len(data_set):
            return []
        return data_set[i:j]
