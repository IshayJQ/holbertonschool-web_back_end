#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays"""
    mlist = []
    for i in range(n):
        mlist.append(await wait_random(max_delay))
    return sorted(mlist)
