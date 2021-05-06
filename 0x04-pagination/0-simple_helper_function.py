#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """a list for those particular pagination parameters

    Args:
        page (int): [description]
        page_size (int): [description]

    Returns:
        tuple: start index and an end index corresponding to the
        range of indexes
    """
    return (page - 1) * page_size, page * page_size
