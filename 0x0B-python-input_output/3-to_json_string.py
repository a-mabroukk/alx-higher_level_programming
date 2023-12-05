#!/usr/bin/python3
""" import the JSON module"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)"""
    to_JSON_string = json.dumps(my_obj)
    return to_JSON_string
