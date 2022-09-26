#!/usr/bin/python3

"""
    Improved BaseGeometry class from 6-base_geometry
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
