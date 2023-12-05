#!/usr/bin/python3
"""import JSON module"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text
    file, using a JSON representation
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        save_object_to_file = json.dump(my_obj, f)
