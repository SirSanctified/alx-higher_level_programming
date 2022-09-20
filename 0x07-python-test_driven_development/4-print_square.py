#!/usr/bin/python3

"""
    There is only one function in this module, ``print_square()``
    it prints the square with character #
"""


def print_square(size):
    """
        Print a square to stdout using the # character

        :size: the length of the square
        :return: nothing
    """
    if type(size) == int and size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    size = int(size)
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

