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
                Otherwise, return the JSON string representation of
                    list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

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
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
            returns the list of the JSON string representation json_string:

                json_string is a string representing a list of dictionaries
                If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            returns an instance with all attributes already set:

            **dictionary can be thought of as a double pointer to a dictionary
            To use the update method to assign all attributes, you must create
            a “dummy” instance before:
                Create a Rectangle or Square instance with “dummy”
                    mandatory attributes (width, height, size, etc.)
                Call update instance method to this “dummy”
                    instance to apply your real values
                must use the method def update(self, *args, **kwargs)
            **dictionary must be used as **kwargs of the method update
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances:

            The filename must be: <Class name>.json - example: Rectangle.json
            If the file doesn’t exist, return an empty list
            Otherwise, return a list of instances - the type of these
                instances depends on cls (current class using this method)
            Must use the from_json_string and create methods
                (implemented previously)
        """
        filename = "{}.json".format(cls.__class__.__name__)
        try:
            with open(filename, encoding='utf-8') as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            serializes in CSV:

            The filename must be: <Class name>.csv - example: Rectangle.csv
            Has the same behavior as the JSON serialization/deserialization
            Format of the CSV:
                Rectangle: <id>,<width>,<height>,<x>,<y>
                Square: <id>,<size>,<x>,<y>
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'length', 'height', 'x', 'y']
                else:
                    fields = ['id', 'size', 'x', 'y']

                writer = csv.DictWriter(csvfile, fieldname=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
            deserializes in CSV:

            The filename must be: <Class name>.csv - example: Rectangle.csv
            Has the same behavior as the JSON serialization/deserialization
            Format of the CSV:
                Rectangle: <id>,<width>,<height>,<x>,<y>
                Square: <id>,<size>,<x>,<y>
        """
        file_name = cls.__name + ".csv"
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                else:
                    fields = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(csvfile, fieldnames=fields)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in reader]
        except IOError:
            return []
