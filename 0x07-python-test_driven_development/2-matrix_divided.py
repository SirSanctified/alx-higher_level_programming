#!/usr/bin/python3

"""
    This module contains one function that accepts two arguments
    a matrix and an integer/float to divide each element of the matrix
"""

def matrix_divided(matrix, div):
    """
        Attempt to divide each element of ``matrix`` with div

        :matrix: should be a list of lists of integer/float,
                with the same row sizes
        :div: should be an integer/float greater or less than 0
                but not equal to zero
        :return: a new matrix of the same size as ``matrix``,
                but containing each element of ``matrix``
                divided by ``div``
    """

    if not len(set(map(len, matrix))) == 1:
        """
            check if matrix has rows of the same size
        """
        raise TypeError("Each row of the matrix must have the same size")

    if not (all(isinstance(element, list) for element in matrix) and (
             all([isinstance(i, int) for items in matrix for i in items])
            or all([isinstance(i, float) for items in matrix for i in items])
            )):
        """
            check if ``matrix`` is list of lists of integers/floats
        """
        raise TypeError("matrix must be a matrix (list of lists) "
        + "of integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not type(div) in [int, float]:
        raise TypeError("div must be a number")

    return [[round(i / 3, 2) for i in items] for items in matrix]
