#!/usr/bin/python3
"""class Square definition."""


class Square:
    """a class defines crucial for a square by: Private instance attribute

    Attributes:
        size: size of square
    """
    @property
    def size(self):
        """property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set it"""
        self.__size = value

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        """Creates new instances of square."""

        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
