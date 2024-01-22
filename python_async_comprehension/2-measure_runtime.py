#!/usr/bin/env python3
""""
execute async_comprehension four times in parallel using asyncio.gather
"""
from asyncio import gather
from typing import List
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime executed four times in parallel
    """
    start_time: float = time.time()

    """
    Execute async_comprehension four times in parallel using asyncio.gather
    """
    await gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time: float = time.time()
    total_runtime: float = end_time - start_time

    return total_runtime
