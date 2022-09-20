#!/usr/bin/python3

"""
    This modue contains a function that prints out the name to the console
    The other one, ``is_number()`` is a helper to check if a given argument
    is really a string
"""

def is_number(string):
    """
        Check if ``string`` does not represent any number
    """
    try:
        complex(string)
        return True
    except ValueError:
        return False


def say_my_name(first_name, last_name=""):
    """
        Print the name and the last name to the console
        only if they are strings
        return nothing
    """
    if is_number(first_name):
        raise TypeError("first_name must be a string")
    if is_number(last_name):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
