#!/usr/bin/python3
"""
Module for the add_integer function.

This module provides a function that adds two numbers
and returns sum. The arguments must be
integers or floats, otherwise a TypeError is raised.
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns an integer.

    The arguments a and b must be integers or floats.
    If they are floats, they are first converted to integers.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
