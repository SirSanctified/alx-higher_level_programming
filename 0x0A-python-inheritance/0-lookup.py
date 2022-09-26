#!/usr/bin/python3

"""
    This module defines only one function called lookup
"""


def lookup(obj):
    """
        returns the list of available attributes and methods of an object
    """
    return list(dir(obj))

