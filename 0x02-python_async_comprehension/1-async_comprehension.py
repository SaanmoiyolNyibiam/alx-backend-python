#!/usr/bin/env python3
"""
This is a module that defines a coroutine called async_comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This is a coroutine that returns a list generated from
    an async list comprehension
    """
    return_list = [i async for i in async_generator()]
    return return_list
