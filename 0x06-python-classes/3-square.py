#!/usr/bin/python3
"""class Square definition."""


class Square:
    """a class defines crucial for a square by: Private instance attribute

    Attributes:
        size: size of square
    """
    def __init__(self, size=0):
        """New instance of square"""

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""

        return self.__size * self.__size
