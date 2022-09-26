#!/usr/bin/python3

"""
    Create a Rectangle class that inherits from BaseGeometry class
"""


class BaseGeometry:
    """
        Define the area method but do not implement it
    """
    def area(self):
        """
            Raise an exception since not yet implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Perform various checks to validate an integer supplied
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(name) is not str:
            raise TypeError("name must be a string")


class Rectangle(BaseGeometry):
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

    def area(self):
        """
            Implementing the area method
        """
        return self.__width * self.__height

    def __str__(self):
        """
            string representation of Rectangle
        """
        return "[{}] {}/{}".format("Rectangle", self.__width, self.__height)
