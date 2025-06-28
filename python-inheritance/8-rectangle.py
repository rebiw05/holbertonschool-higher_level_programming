#!/usr/bin/python3
"""This module has a class"""


class BaseGeometry:
    """This is a class."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integers."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    this is the rectangle class
    """
    def __init__(self, width, height):
        """
        this is the function
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
