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
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    """static method that returns the list of the JSON
    string representation json_string
    """
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        else:
            JSON_to_Object = json.loads(json_string)
            return JSON_to_Object

    """class method def create(cls, **dictionary): that returns
    an instance with all attributes already set
    """
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''Loads string from file and unjsonifies.'''
        try:
            with open(cls.__name__ + ".json", 'r') as f:
                json_file = Base.from_json_string(f.read())
                return [cls.create(**dct) for dct in json_file]
        except IOError:
            return []
