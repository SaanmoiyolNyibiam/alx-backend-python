#!/usr/bin/env python3
"""
This is a module that defines a task_wait_n routine
"""
from asyncio import as_completed
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This is a function that spawns wait_random
    and returns a list of all the delays
    """
    tasks = []
    delays = []
    for _ in range(n):
        value = task_wait_random(max_delay)
        tasks.append(value)

    for task in as_completed((tasks)):
        delay = await task
        # Insert the delay in the correct order manually (ascending)
        delays.append(delay)
    return delays
