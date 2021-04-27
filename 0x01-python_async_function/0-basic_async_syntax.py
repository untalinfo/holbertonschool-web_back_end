#!/usr/bin/env python3
import random
import asyncio


async def wait_random(max_delay = 10):
    await asyncio.sleep(random.randrange(0, max_delay))
    return max_delay
