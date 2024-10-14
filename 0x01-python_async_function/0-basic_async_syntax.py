#!/usr/bin/env python3
"""This is a module that defines a wait_random function"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """This is a function that waits for a random delay and returns it"""
    delay_time = uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
