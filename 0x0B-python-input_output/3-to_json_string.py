#!/usr/bin/python3

"""
    Define a function that returns the json representation of an object
"""

import json


def to_json_string(my_obj):
    """
        return json representation of @my_obj
    """
    return json.dumps(my_obj)
