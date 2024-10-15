#!/usr/bin/env python3
"""
This is a module that defines the async_generator function
"""
from typing import AsyncGenerator
from random import uniform
from asyncio import sleep


async def async_generator() -> AsyncGenerator[float, None]:
    """This is an async generator"""
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
