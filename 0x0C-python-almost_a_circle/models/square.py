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

    def __str__(self):
        """Return a string with the characteristic of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
