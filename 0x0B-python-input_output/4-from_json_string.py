#!/usr/bin/python3

"""
    Deserialise a json string to an object
"""

import json


def from_json_string(my_str):
    """
        return an object represented by my_str
    """
    return json.loads(my_str)
