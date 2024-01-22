#!/usr/bin/env python3
"""
Coroutine that loops 10 times, asynchronously waits 1 second,
and yields a random number between 0 and 10.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, NoneType, NoneType]:
    """
    Generate the random number.
    """
    for loops in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
