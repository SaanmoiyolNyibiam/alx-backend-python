#!/usr/bin/env python3
"""
This is a module that defines a measure_time function
"""
from time import perf_counter
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This is a function that measures the total execution time for
    the wait_n routine
    """
    initial_time = perf_counter()
    run(wait_n(n, max_delay))
    final_time = perf_counter()
    total_time = final_time - initial_time
    return total_time/n
