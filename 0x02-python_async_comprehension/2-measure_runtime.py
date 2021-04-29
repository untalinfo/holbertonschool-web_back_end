#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return it.

    Returns:
        float: [description]
    """
    tks = []
    t_time = time.time()
    [tks.append(asyncio.create_task(async_comprehension())) for i in range(4)]
    await asyncio.gather(*tks)
    return time.time() - t_time
