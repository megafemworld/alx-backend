#!/usr/bin/env python3
"""
1-simple_pagination.py

This module provides a simple pagination system for handling a dataset.
It includes functions and a class to manage data pagination.

Classes:
- Server: Manages the dataset and provides paginated views.

Functions:
- index_range(page, page_size): Calculates the start
and end indices for pagination.
"""

from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start
        and end indices for the page.
    """
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return (start, end)


class Server:
    """
    Server class to paginate a dataset of popular baby names.

    Attributes:
        DATA_FILE (str): The path to the CSV file containing the dataset.

    Methods:
        dataset(): Loads and caches the dataset.
        get_page(page, page_size): Retrieves a specific page of the dataset.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance and prepare the dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        Returns:
            List[List]: The dataset as a list of rows, excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of the dataset.

        Args:
            page (int): The page number to retrieve (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows representing the requested
            page of the dataset, or an empty list if the page is
            out of range.

        Raises:
            AssertionError: If page or page_size is not an
            integer or is less than 1.
        """
        assert isinstance(page, int) and isinstance(page_size, int), \
            "Both page and page_size must be integers."
        assert page > 0 and page_size > 0, \
            "Both page and page_size must be greater than 0."

        start_index, end_index = index_range(page, page_size)

        # If the start index is out of range, return an empty list
        if start_index >= len(self.dataset()):
            return []

        # Return the paginated data slice
        return self.dataset()[start_index:end_index]
