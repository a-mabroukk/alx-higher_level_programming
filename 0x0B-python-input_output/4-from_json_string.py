#!/usr/bin/python3
"""import json module"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by JSON string"""
    JSON_to_Object = json.loads(my_str)
    return JSON_to_Object
