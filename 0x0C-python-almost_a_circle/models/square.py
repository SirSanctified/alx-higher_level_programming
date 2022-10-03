#!/usr/bin/python3

"""
    In this module I will:

        Write the class Square that inherits from Rectangle:

            Class Square inherits from Rectangle
            Class constructor: def __init__(self, size, x=0, y=0, id=None)::
                Call the super class with id, x, y, width and height
                        - this super call will use the logic of the __init__
                        of the Rectangle class.
                The width and height must be assigned to the value of size
                No new attributes created for this class,
                    use all attributes of Rectangle
                All width, height, x and y validation must inherit from
                    Rectangle - same behavior in case of wrong data
    The overloading __str__ method should return
        [Square] (<id>) <x>/<y> - <size> - in our case, width or height
"""

import models.rectangle


class Square(models.rectangle.Rectangle):
    """
        Inherit all methods and attributes from Rectangle and only define new
        width and height
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initialise a square with same width and height
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            Override the defualt __str__ method from Rectangle
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.width)

    @property
    def size(self):
        """
            getter for size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
            Setter for size using the logic from Rectangle's width setter
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
            assigns attributes:

                *args is the list of arguments - no-keyworded arguments
                    1st argument should be the id attribute
                    2nd argument should be the size attribute
                    3rd argument should be the x attribute
                    4th argument should be the y attribute
                **kwargs can be thought of as a double pointer to a
                    dictionary: key/value (keyworded arguments)
                **kwargs must be skipped if *args exists and is not empty
                Each key in this dictionary represents an attribute to the
                    instance
        """

        if len(args) > 0:
            attrs = [self.id, self.size, self.x, self.y]
            for i in range(len(args)):
                attrs[i] = args[i]
            self.id = attrs[0]
            self.size = attrs[1]
            self.x = attrs[2]
            self.y = attrs[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Square
        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
