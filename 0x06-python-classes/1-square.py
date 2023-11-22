#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: Private instance attribute

    Attributes:
        size: size of a square
    """
    def __init__(self, size):
        """Creates new instances of square."""

        self.__size = size
