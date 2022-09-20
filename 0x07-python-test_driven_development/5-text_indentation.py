#!/usr/bin/python3

"""
    This module contains a function that prints a text with 2 new lines.
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        Print a text with 2 new lines after each of these
        characters: ., ? and :
    """

    splitters = [".", "?", ":"]
    sentence = ""
    txt = []

    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        sentence = sentence + i
        if i in splitters:
            txt.append(sentence.strip())
            sentence = ""
    for j in txt:
        print(j)
        print()
