#!/usr/bin/python3

"""
this module is a based on 2-square.py, but contains type checking
"""


class Square:
    """ Square class definition """
    def __init__(self, size=0):
        """ class initialization """
        self.size = size

    @property
    def size(self):
        """ getter """
        return self.__size

    @size.setter
    def size(self, size):
        """ setter """
        if not type(size) == int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ calculate the area of this square """
        return self.size ** 2
