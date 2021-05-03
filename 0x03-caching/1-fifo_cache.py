#!/usr/bin/python3
"""
FIFO caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Base FIFOcache class inhert BaseCaching
    """
    def __init__(self):
        """
        Constructor Method
        """
        super().__init__()
        self.list_name = []

    def put(self, key, item):
        """
        Put Method
        """
        if key is None or item is None:
            return None

        self.cache_data[key] = item

        if key not in self.list_name:
            self.list_name.append(key)
        else:
            if self.list_name[-1] != key:
                self.list_name.remove(key)
                self.list_name.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.list_name[0]
            print('DISCARD: {}'.format(discard))
            del self.cache_data[discard]
            self.list_name.pop(0)

    def get(self, key):
        """
        Get Method
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
