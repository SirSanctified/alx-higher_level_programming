#!/usr/bin/python3

"""
    Define a function that writes text to a file
"""


def write_file(filename="", text=""):
    """
       write text to file
    """
    if filename != '':
        with open(filename, 'w', encoding='utf-8') as f:
            return f.write(text)
