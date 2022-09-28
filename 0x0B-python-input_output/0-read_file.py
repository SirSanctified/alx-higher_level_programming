#!/usr/bin/python3

"""
    Read a file and print its contents to the stdout
"""


def read_file(filename=""):
    """
        Open and read the file
    """
    if filename:
        with open(filename, 'r', encoding="utf-8") as file:
            print(file.read(), end="")
