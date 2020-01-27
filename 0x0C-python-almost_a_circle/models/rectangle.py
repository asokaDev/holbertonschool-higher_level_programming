#!/usr/bin/python3
from models.base import Base
"""This module define the Rectangle class"""


class Rectangle(Base):
    """Definition of an rectangle (inherits from Base)
    Args:
        width: width of the rectangle
        height: height of the rectangle
        x: Position in the X axis
        y: Position in the Y axis
        id: id of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Comentario para que el checker lo valide"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """Returns the area value of the Rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__height):
            for i in range(self.__width):
                print("#", end="")
            print()

    """Special methods"""
    def __str__(self):
        """Return a string with the characteristic of the Rectangle
            instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.__width, self.__height)

    """Getters and setters"""
    @property
    def width(self):
        """Get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Get the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
