#!/usr/bin/python3
"""definition class"""


class Rectangle:
    """defines a rectangle by: Private instance attribute"""

    number_of_instances = 0
    print_symbol = "#"

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

        type(self).number_of_instances += 1

    def area(self):
        """returns the rectangle area"""

        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""

        if self.__width == 0:
            return 0
        if self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """ return the rectangle with the character #
        """
        string = ""
        if self.__width == 0:
            return string
        if self.__height == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                print("{:s}".format(str(self.print_symbol)), end="")
            if i != self.__height - 1:
                print()
        return ""

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of a class"""
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """static method returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """class method return a new Rectangle instance"""
        return cls(size, size)
