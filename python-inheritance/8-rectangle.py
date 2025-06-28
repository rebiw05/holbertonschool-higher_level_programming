#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from BaseGeometry.
"""


class BaseGeometry:
    """This is a class."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integers."""
        if type(value) is not int or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Must be a positive.
            height (int): The height of the rectangle. Must be a positivee.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
