#!/usr/bin/python3

"""
    This module contains only one function to add two integer numbers
    The function is called ``add_integer``
    It returns the sum of two integers passed in as parameters
"""


def add_integer(a, b=98):
    """
        Add two integer numbers. If provided with float numbers,
        they are first casted to integers befor being added.
        If either @a or @b are neither integer nor float,
        a TypeError exception is raised

        :a: first integer number for addition
        :b: optional second integer for addition
        :return: the sum of of `a` and `b`
    """

    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
