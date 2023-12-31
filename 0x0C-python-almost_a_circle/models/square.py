#!/usr/bin/python3
"""inheriting class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class constructor"""
    def __init__(self, size, x=0, y=0, id=None):
        """Call the super class with id - this super call with use the logic
        of the __init__ of the Rectangle class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return , [Square] (<id>) <x>/<y> - <size> - in our case,
        width or height
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """property to retrieve it"""
        return self.width

    @size.setter
    def size(self, value):
        """property setter to set it"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign attributes"""
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """public method that returns the dictionary representation of a
        Square
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
