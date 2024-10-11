#!/usr/bin/env python3
"""This is a module that defines a sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mixed_list: List[Union[int, float]]) -> float:
    """sums up a list of mixed types and return a float"""
    sum_total: float = 0
    for value in mixed_list:
        sum_total += value
    return sum_total
