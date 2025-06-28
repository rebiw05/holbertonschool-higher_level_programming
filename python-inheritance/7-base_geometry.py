#!/usr/bin/python3
"""
this defines empty class and functions
"""


class BaseGeometry:
    """
    this is empty class
    """

    def area(self):
        """
        this raise an error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        this validates the value
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
