#!/usr/bin/python3

"""
    Create a Rectangle class that inherits from BaseGeometry class
"""


class Rectangle((BaseGeometry):
    """
        Implement all the functionality of BaseGeometry
        Add extra functionality
    """
    def __init__(self, width, height):
        """
            initialise the rectangle object
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
