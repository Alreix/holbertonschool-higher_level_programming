#!/usr/bin/python3
"""Module for text_indentation.

This module defines the function text_indentation(text)
that prints a text with 2 new lines after each '.', '?'
and ':' character, without leading or trailing spaces
on each printed line.
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'.
    Args:
        text: the text to process, must be a string.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current = ""

    for char in text:
        current += char
        if char in ".?:":
            print(current.strip())
            print()
            print()
            current = ""

    if current.strip() != "":
        print(current.strip(), end="")
