#!/usr/bin/python3
"""a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix.
    
    Args:
        matrix: the matrix
        div: the number to divide by
    Raise:
        TypeError: if the number is not int or float
        if matrix is not of same size 
        div is not a number
        ZeroDivisionError: div cant be zero
    Return:
        New matrix
    """
    matrixl = 0

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if matrixl != 0 and len(row) != matrixl:
            raise TypeError("Each row of the matrix must have the same size")

        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        matrixl = len(row)

    s = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (s)