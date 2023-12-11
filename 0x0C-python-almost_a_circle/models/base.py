#!/usr/bin/python3
"""Definition of class"""
import json


class Base:
    """private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """static method that returns the JSON string representation of
    list_dictionaries
    """
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == [{}]:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    """class method that writes the JSON string representation of
    list_objs to a file
    """
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs.write("[]")
        else:
            list_objs = [o.to_dictionary() for o in list_objs]
            with open("{}.json".
                      format(cls.__name__), "w", encoding="utf-8") as f:
                if list_objs is None:
                    f.write("[]")
                f.write(Base.to_json_string(list_objs))
