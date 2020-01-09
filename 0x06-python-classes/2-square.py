#!/usr/bin/env python3
class Square():
    """ Class than define a square

    """

    def __init__(self, size=0):
        self.__size = size
        if size not is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
