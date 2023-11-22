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
    
    def __init__(self, size=0, position=(0, 0)):
        """New instances of square."""

        self.size = size
        self.position = position

    @property
    def position(self):
        """Returns the position of the square"""

        return self.__position
    
    @position.setter
    def position(self, value):
        """property setter to set it"""
    
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
