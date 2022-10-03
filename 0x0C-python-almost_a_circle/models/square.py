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
        super().__init__(self.size, self.size, x, y, id)

    def __str__(self):
        """
            Override the defualt __str__ method from Rectangle
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                                self.id,
                                                self.x,
                                                self.y,
                                               self.width)