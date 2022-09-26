#!/usr/bin/python3

"""
    Check if an object is a subclass of a supplied class
"""


def inherits_from(obj, a_class):
    """
        Return True if obj is subclass of a_class else False
    """
    return issubclass(obj.__class__, a_class)
