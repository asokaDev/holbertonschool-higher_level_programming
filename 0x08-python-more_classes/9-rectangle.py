#!/usr/bin/python3
"""
    This module define a Rectangle and the operations that are possible
    with this
"""


class Rectangle():
    """Define a rectangle.

    Args:
        width: width of the rectangle (integer)
        height:height of the rectangle (integer)
    """

    number_of_instances = 0
    """int: number of rectangles that exist in every moment"""
    print_symbol = "#"
    """any type: Symbol to print the representation of the rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Destructor

        Print a message when a rectangle is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """Get the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Print the rectangle with the character indicated by print_symbol"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.__height):
                rect += str(self.print_symbol) * self.__width
                if i < self.__height - 1:
                    rect += "\n"
        return rect

    def __repr__(self):
        """Return a string that represent the actual state of the object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def area(self):
        """Method that return the area of the square"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that return the area of the square"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area
        Args:
            rect_1: An instance of Rectangle
            rect_2: An instance of Rectangle
        Returns:
            Rectangle: The rectangle of bigger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
