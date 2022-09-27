#!/usr/bin/python3
import json

"""
    Deserialise a json string to an object
"""


def from_json_string(my_str):
    """
        return an object represented by my_str
    """
    return json.loads(my_str)
