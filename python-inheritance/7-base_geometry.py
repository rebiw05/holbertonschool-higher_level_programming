#!/usr/bin/python3
"""
This module defines a base geometry class.
"""

class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raises an exception as area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
