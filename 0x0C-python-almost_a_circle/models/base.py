#!/usr/bin/python3

"""
    The class defined here will be the “base” of all other classes
    in this project. The goal of it is to manage id attribute in all
    future classes and to avoid duplicating the same code
    (by extension, same bugs)
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            that returns the JSON string representation of list_dictionaries:

                list_dictionaries is a list of dictionaries
                If list_dictionaries is None or empty, return the string: "[]"
                Otherwise, return the JSON string representation of list_dictionaries
        """
        json_string = '['
        for i in list_dictionaries:
            json_string += json.dumps(i)
        return json_string + ']'

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON string representation of list_objs to a file:
                > list_objs is a list of instances who inherits of Base 
                    - example: list of Rectangle or list of Square instances
                > If list_objs is None, save an empty list
                > The filename must be: <Class name>.json 
                    - example: Rectangle.json
                > Uses the static method to_json_string (created before)
                > Overwrite the file if it already exists
        """
        filename = "{}.json".format(cls.__class__.__name__)
        json_string = cls.to_json_string(list_objs)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(json_string, filename)
