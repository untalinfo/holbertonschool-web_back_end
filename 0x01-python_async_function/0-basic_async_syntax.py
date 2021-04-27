#!/usr/bin/env python3
"""
The basics of async
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """takes in an integer argument (max_delay, with a default value of 10)
    named wait_random that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.

    Args:
        max_delay (int, optional): delay. Defaults to 10.

    Returns:
        [type]: [description]
    """
    number: float = random.uniform(0, max_delay)
    await asyncio.sleep(number)
    return number
