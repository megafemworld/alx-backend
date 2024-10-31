#!/usr/bin/env python3
from base_caching import BaseCaching
"""BasicCache that inherits from BaseCaching and is a caching system"""


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary.
    """

    def put(self, key, item):
        """
            Assign value for the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
             return the value linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
