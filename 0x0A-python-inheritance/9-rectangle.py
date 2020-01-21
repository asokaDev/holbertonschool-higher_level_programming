#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Rectangle module"""


class Rectangle(BaseGeometry):
    """Definition of an rectangle"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
