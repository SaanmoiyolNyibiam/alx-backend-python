#!/usr/bin/env python3
"""
This is module that defines a measure_time function
"""
from time import perf_counter
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This is a coroutine the measure the runtime
    of another coroutine
    """
    initial_time = perf_counter()

    await gather(async_comprehension(),
                 async_comprehension(),
                 async_comprehension(),
                 async_comprehension())

    final_time = perf_counter()
    total_time = final_time - initial_time
    return total_time
