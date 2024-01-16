#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    final_time = time.perf_counter() - start_time
    return final_time / n
