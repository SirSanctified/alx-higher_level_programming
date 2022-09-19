#!/usr/bin/python3

"""
    This module defines a rectangle class based on 0-rectangle.py
"""


class Rectangle:
    """
        Definition of the rectangle class and its getters and setters
    """
    def __init__(self, width=0, height=0):
        """
            Rectangle initialization
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            Getter for width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
            Setter for width
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
            Getter for height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
            Setter for height
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
