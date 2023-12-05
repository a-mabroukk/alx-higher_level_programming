#!/usr/bin/python3
"""class definition"""


class Student:
    """Instantiation class with"""
    def __init__(self, first_name, last_name, age):
        """Instantiation Public instance attributes with"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a
          Student instance (same as 8-class_to_json.py)
          """
        return self.__dict__
