#!/usr/bin/python3
"""inheriting class"""
from models.base import Base


class Rectangle(Base):
    """Class constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Call the super class with id - this super call with use the logic
        of the __init__ of the Base class
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
    @property
    def x(self):
        """property to retrieve it"""
        return self.__x

    @x.setter
    def x(self, value):
        """property setter to set it"""
        self.__x = value

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """property to retrieve it"""
        return self.__y

    @y.setter
    def y(self, value):
        """property setter to set it"""
        self.__y = value

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
    def area(self):
        """adding the public method that returns the area value of
        the Rectangle instance
        """
        return self.__height * self.__width

    def display(self):
        """adding the public method that prints in stdout the Rectangle"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if i != self.__height * 4:
                print()
        return ""

    def __str__(self):
        """it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            type(self).__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute"""

        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """public method that returns the dictionary representation of a
        Rectangle
        """
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
