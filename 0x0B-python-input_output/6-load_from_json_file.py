#!/usr/bin/python3

"""
    load an object from text file
"""

import json


def load_from_json_file(filename):
    """
        Deserialize a json object from @filename
    """
    
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
