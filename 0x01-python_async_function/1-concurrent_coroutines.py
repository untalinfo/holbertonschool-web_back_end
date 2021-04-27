#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int, n: int) -> List[float]:
    """takes in 2 int arguments (in this order): n and max_delay. You will
    spawn wait_random n times with the specified max_delay.

    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency.

    Args:
        n (int): repetitions number
        max_delay (int): delay

    Returns:
        List[float]: array of elements
    """
    delays: List[float] = []
    all_delays: List[float] = []

    for _ in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays
