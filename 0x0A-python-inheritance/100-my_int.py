#!/usr/bin/python3

"""
    Override the == and != operators of the integer class
"""


class MyInt(int):
    """
        invert the == and != operators
    """

    def __eq__(self, other):
        """
            invert the == operator
        """
        return True if self != other else False

    def __ne__(self, other):
        """
            invert the != operator
        """
        return True if self == other else False
