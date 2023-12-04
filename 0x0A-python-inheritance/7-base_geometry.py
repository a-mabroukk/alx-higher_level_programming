#!/usr/bin/python3
"""class definition"""


class BaseGeometry:
    """Public instance method"""
    def area(self):
        """ raises an Exception with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
