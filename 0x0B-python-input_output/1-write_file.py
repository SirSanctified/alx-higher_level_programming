#!/usr/bin/python3

"""
    Define a function that writes text to a file
"""


def write_file(filename='', text=''):
    """
        write @text to @filename
    """
    if filename:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
