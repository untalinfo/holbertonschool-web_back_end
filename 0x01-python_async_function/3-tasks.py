#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """takes an integer max_delay and returns a asyncio.Task.

    Args:
        max_delay (int): delay

    Returns:
        [type]: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
