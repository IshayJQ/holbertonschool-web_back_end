#!/usr/bin/env python3
"""Asynchronous coroutine that waits for a random delay"""

from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Return the random delay between 0 and max_delay seconds
    """
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
