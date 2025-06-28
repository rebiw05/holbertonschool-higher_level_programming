#!/usr/bin/python3
"""
This module defines the BaseGeometry class
and value validation.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.
    """

    def area(self):
        """
        Calculates the area of the geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value to ensure it is an integer greater than 0.
        """
        # Check if value is an integer
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        # Check if value is greater than 0
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
