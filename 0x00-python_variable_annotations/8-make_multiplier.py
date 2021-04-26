#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument and returns a function that
    multiplies a float by multiplier.

    Args:
        multiplier (float): number float

    Returns:
        Callable[[float], float]: [description]
    """
    return lambda x: x * multiplier
