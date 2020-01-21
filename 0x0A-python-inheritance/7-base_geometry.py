#!/usr/bin/python3
"""Base Geometry module"""


class BaseGeometry():
    """Base class"""
    def area(self):
        """Unimplemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate an integer"""
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
