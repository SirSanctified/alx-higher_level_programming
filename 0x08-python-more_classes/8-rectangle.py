#!/usr/bin/python3

"""
    This module defines a rectangle class based on 7-rectangle.py
"""


class Rectangle:
    """
        Definition of the rectangle class and its getters and setters
        There is also definition for the area and perimeter methods
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Rectangle initialization
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
                try:
                    st = st + str(self.print_symbol)
                except NameError:
                    st = st + str(type(self).print_symbol)
            if i != self.__height - 1:
                st = st + "\n"
        return st

    def __repr__(self):
        """
            String representation of an object so that it can be recreated
            using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
            print the message to console
        """
        del self
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            determine if 2 rectangle are equal based on their area
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
