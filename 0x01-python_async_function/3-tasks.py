#!/usr/bin/env python3
"""
Tasks
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes an integer max_delay and returns a asyncio.Task.

    Args:
        max_delay (int): delay

    Returns:
        [type]: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
