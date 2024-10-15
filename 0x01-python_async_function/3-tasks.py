#!/usr/bin/env python3
"""
This is a module that defines a task_wait_random function
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This is a function that creates a task and returns it
    """
    return asyncio.create_task(wait_random(max_delay))
