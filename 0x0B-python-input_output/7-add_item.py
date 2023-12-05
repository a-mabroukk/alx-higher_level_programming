#!/usr/bin/python3
"""import JSON module"""
import json


def save_to_json_file(my_obj, filename):
    """a script that adds all arguments to a Python list, and
    then save them to a file
    """
    with open(filename, 'w', encoding='UTF-8') as item:
        json.dump(my_obj, item)
