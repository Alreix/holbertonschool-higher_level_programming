#!/usr/bin/python3
"""Module for matrix_divided.
Defines a function that divides all elements of a matrix
(list of lists) of integers/floats by a number and returns
a new matrix with results rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.
    Args:
        matrix: list of lists of integers or floats.
        div: number (int or float) used as divisor.
    Returns:
        A new matrix with all values divided by div,
        each rounded to 2 decimal places.
    Raises:
        TypeError: If matrix is not a matrix (list of lists)
                   of integers/floats, if rows have different
                   sizes, or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    msg_matrix = "matrix must be a matrix (list of lists) of integers/floats"

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise TypeError(msg_matrix)

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
