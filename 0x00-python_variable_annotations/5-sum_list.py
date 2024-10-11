#!/usr/bin/env python3
"""This is a module that define a sum_list function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """This is a function that adds the sum of the values in a list"""
    total_sum: float = 0
    for value in input_list:
        total_sum += value
    return total_sum
