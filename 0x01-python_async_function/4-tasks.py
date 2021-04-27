#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random is being
    called.

    Args:
        n (int): repetitions number
        max_delay (int): delay

    Returns:
        List[float]: array of elements
    """
    numbers = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(numbers)
