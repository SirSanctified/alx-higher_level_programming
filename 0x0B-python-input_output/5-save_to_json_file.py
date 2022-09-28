#!/usr/bin/python3

"""
    Save a serialized json object to file
"""

import json


def save_to_json_file(my_obj, filename):
    """
        save @my_obj to @filename
    """
    json.load(my_obj, filename)
