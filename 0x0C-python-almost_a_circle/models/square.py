#!/usr/bin/python3
"""
This module define the Square class, that inherits from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Definition of an square (inherits from Rectangle)
    Args:
        size:
        x: Position in the X axis
        y: Position in the Y axis
        id: id of the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Update the attributes of the Square"""
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                if key == 1:
                    self.size = value
                if key == 2:
                    self.x = value
                if key == 3:
                    self.y = value
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """Return a string with the characteristic of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value of size"""
        self.width = value
        self.height = value
