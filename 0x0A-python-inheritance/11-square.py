#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""This module define the Square class in base a Rectangle class"""


class Square(Rectangle):
    """class Square that inherits from Rectangle."""
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
