#!/usr/bin/python3

"""
    Define a function that checks if an object is an instance of a given class
"""


def is_same_class(obj, a_class):
    """
        use isinstance() to check if obj is an instance of a_class
    """
    return type(obj) is a_class
