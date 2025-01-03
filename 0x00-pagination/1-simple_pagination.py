#!/usr/bin/env python3
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    Args:
        page - page number
        page_size - page size
    Return:
        tuple
    """
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
        """Cached dataset to be
        used by get_page method
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Given a page number and page size,
        returns the right page of the dataset
        Args:
            page - page
            page_size - size of page
        Return:
            right page of the dataset, empty list if out of range
        """
        assert isinstance(page, int) and isinstance(page_size, int), \
            "Both page and page_size must be integers."
        assert page > 0 and page_size > 0, \
            "Both page and page_size must be greater than 0."

        start_index, end_index = index_range(page, page_size)
        if ((len(self.dataset()) < start_index) or
                (len(self.dataset()) < end_index)):
            return []

        paginated_names = []
        for i in range(start_index, end_index):
            paginated_names.append(self.dataset()[i])

        return paginated_names
