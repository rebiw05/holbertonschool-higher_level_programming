#!/usr/bin/python3
"""
This module defines rectangle with width and height.
"""


class Rectangle:
    """
    this defines rectangle with atributes

    Attributes:
        width (int): defines width of the rectangle
        __height (int): defines height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        this defines the width and height.

        args:
        width: the size of rectangle
        height (private): the other size of recrangle

        raises: TypeError, ValueError
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
