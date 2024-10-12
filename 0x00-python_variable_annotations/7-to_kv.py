#!/usr/bin/env python3
"""This is a module that defines a to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This is a function that creates a tuple"""
    output: Tuple[str, float] = (k , v*2)
    return output
