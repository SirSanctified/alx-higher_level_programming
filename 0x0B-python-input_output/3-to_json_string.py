#!/usr/bin/python3
import json

"""
    Define a function that returns the json representation of an object
"""


def to_json_string(my_obj):
    """
        return json representation of @my_obj
    """
    return json.dumps(my_obj)
