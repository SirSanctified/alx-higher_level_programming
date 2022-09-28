#!/usr/bin/python3

"""
    Define a function to append text to a file
"""


def append_write(filename='', text=''):
    """
        Append @text to @filename, if @filename doesn't exist, create it
    """
    if filename:
        with open(filename, 'a', encoding='utf-8') as file:
            return file.write(text)
