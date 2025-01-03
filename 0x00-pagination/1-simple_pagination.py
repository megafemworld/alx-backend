#!/usr/bin/env python3
from typing import Tuple
import csv
import math
from typing import List
"""
    The function should return a tuple of size two
    containing a start index and an end index corresponding
    to the range of indexes to return in a list
    for those particular pagination parameters.
"""


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """index_range that takes two integer arguments page and page_size
    and returns a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    args:
        page: int: page number
        page_size: int: number of items per page
    """
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names in chunks.

    Attributes:
        DATA_FILE (str): The path to the CSV file containing the dataset.

    Methods:
        __init__():
            Initializes the Server instance with an empty dataset.
        dataset() -> List[List]:
            Returns the cached dataset. If the dataset is not cached, it reads
            the data from the CSV file and caches it.
        get_page(page: int = 1, page_size: int = 10)
        -> List[List]:
            Returns a list of lists containing the
            paginated data for the specified
            page and page size. If the page or page size is invalid,
            it returns an empty list.
    Server class to paginate a database of popular baby names in chunks
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
        get_page that takes two integer arguments page with default
        value 1 and page_size with default value 10
        and returns a list of lists containing the
        paginated data
        for those arguments:
            page: int: page number
            page_size: int: number of items per page
        """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0

        start_index, end_index = index_range(page, page_size)
        if ((len(self.dataset()) < start_index) or
                (len(self.dataset()) < end_index)):
            return []

        paginated_names = []
        for i in range(start_index, end_index):
            paginated_names.append(self.dataset()[i])

        return paginated_names
