#!/usr/bin/python3

"""
    This module contains  Rectangle class which extends the Base
"""
from models.base import Base


class Rectangle(Base):
    """
        Initialise a rectangle with the width, height and
        it's x and y coordinates
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initialise the id using the logic employed in base
            Other attributes must be initialised as per this class's logic
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
            getter for @__width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
            validate and set the width attribute
        """
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(width) != 'int':
            raise TypeError("width must be an integer")
        self.__width = width

    @property
    def height(self):
        """
            getter for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
            validate and set the height attribute
        """
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(height) != 'int':
            raise TypeError("height must be an integer")
        self.__height = height

    @property
    def x(self):
        """
            getter for x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
            validate and set x attribute
        """
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(x) != 'int':
            raise TypeError("x must be an integer")
        self.__x = x

    @property
    def y(self):
        """
            getter for y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
            validate and set y
        """
        if y < 0:
            raise ValueError("y must be >= 0")
        if type(y) != 'int':
            raise TypeError("y must be an integer")
        self.__y = y

    def area(self):
        """
            return the area value of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            print a rectangle representation using `#`
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
            Override the defualt __str__ method from object
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id,
                                                self.x,
                                                self.y,
                                                self.width,
                                                self.height)
