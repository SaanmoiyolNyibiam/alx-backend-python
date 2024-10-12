#!/usr/bin/env python3
"""This is a module that defines a make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This is a function that takes a float(multiplier) and return a function
    that multiplies a float by the multiplier
    """
    def sub_make_multipler(sub_multiplier: float):
        """Multiplies sub_multiplier by multiplier"""
        return float(sub_multiplier * multiplier)
    return sub_make_multipler
