#!/usr/bin/python3
"""import JSON module"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file"""
    with open(filename, 'r') as json_file:
        create_JSON_file = json.load(json_file)
        return create_JSON_file
