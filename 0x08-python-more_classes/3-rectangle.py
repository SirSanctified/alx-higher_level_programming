#!/usr/bin/python3

"""
    This module defines a rectangle class based on 2-rectangle.py
"""


class Rectangle:
    """
        Definition of the rectangle class and its getters and setters
        There is also definition for the area and perimeter methods
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

    def area(self):
        """
            Calculate the area of the rectangle
            use the formula height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Calculate the perimeter of the rectange
            Use the formular 2 * (height + width)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
            Print the string representation of the object
        """
        st = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                st = st + "#"
            if i != self.__height - 1:
                st = st + "\n"
        return st
