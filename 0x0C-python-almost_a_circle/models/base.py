#!/usr/bin/python3

"""
    The class defined here will be the “base” of all other classes
    in this project. The goal of it is to manage id attribute in all
    future classes and to avoid duplicating the same code
    (by extension, same bugs)
"""


class Base:
    """
        This class only handles the initialization part with the id attribute
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
            Initialise the `id` with the number of instances if supplied id is
            None
        """
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
