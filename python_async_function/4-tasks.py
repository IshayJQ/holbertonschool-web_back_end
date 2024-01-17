#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays"""
    mlist = []
    for i in range(n):
        mlist.append(await task_wait_random(max_delay))
    return sorted(mlist)
