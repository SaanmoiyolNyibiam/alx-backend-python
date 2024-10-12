#!/usr/bin/env python3
"""This is a function that defines an element_length function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This is a function that returns an iterable"""
    return [(i, len(i)) for i in lst]
