#!/usr/bin/env python3
"""This is a function that defines a safely_get_value function"""
from typing import Union, Any, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """This is a function that checks for a key in a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
