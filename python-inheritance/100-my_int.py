#!/usr/bin/python3
"""Module that defines MyInt, an int subclass with inverted equal operators"""


class MyInt(int):
    """MyInt is a rebel integer that inverts == and != comparisons."""

    def __eq__(self, other):
        """Return the inverted result of the normal equality comparison."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Return the inverted result of the normal inequality comparison."""
        return int.__eq__(self, other)
