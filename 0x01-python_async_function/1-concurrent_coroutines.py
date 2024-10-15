#!/usr/bin/env python3
"""This is a module that defines a wait_n async routine"""
from asyncio import as_completed
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This is a function that spawns wait_random
    and returns a list of all the delays
    """
    tasks = []
    delays = []
    for _ in range(n):
        value = wait_random(max_delay)
        tasks.append(value)

    for task in as_completed((tasks)):
        delay = await task
        # Insert the delay in the correct order manually (ascending)
        delays.append(delay)
    return delays
