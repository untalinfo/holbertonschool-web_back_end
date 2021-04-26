#!/usr/bin/env python3
"""
    function safe_first_element with annotations
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return the first element of lst if it exists """
    if lst:
        return lst[0]
    else:
        return None
