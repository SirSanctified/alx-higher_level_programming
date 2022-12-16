#!/usr/bin/python3
""" This module contains a function that returns a peak """


def find_peak(list_of_integers):
    """ Finds a peak in a list of integers """
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
