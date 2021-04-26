#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list mxd_lst of integers and floats and returns their
    sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): list contains integers or floats

    Returns:
        float: sum of elements
    """
    return sum(mxd_lst)
