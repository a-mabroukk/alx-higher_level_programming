#!/usr/bin/python3
"""class definition"""


class Student:
    """Instantiation class with"""
    def __init__(self, first_name, last_name, age):
        """Instantiation Public instance attributes with"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a
          Student instance (same as 8-class_to_json.py)
          """
        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary

    def reload_from_json(self, json):
        """Public method that replaces all attributes of Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
