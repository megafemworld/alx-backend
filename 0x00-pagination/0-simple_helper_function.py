#!/usr/bin/env python3
from typing import Tuple
"""
    The function should return a tuple of size two
    containing a start index and an end index corresponding
    to the range of indexes to return in a list
    for those particular pagination parameters.
"""


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """index_range that takes two integer arguments page and page_size"""
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return start, end
