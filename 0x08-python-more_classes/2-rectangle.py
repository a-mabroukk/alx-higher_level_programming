#!/usr/bin/python3
"""definition class"""


class Rectangle:
    """defines a rectangle by: Private instance attribute"""
    @property
    def width(self):
        """property to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set it"""
        self.__width = value

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """property to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter to set it"""
        self.__height = value

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def __init__(self, width=0, height=0):
        """New instance of rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """returns the rectangle area"""

        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""

        if self.width == 0:
            return 0
        if self.height == 0:
            return 0
        return self.__height + self.__width
