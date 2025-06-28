#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from BaseGeometry.
"""

# Assuming BaseGeometry is defined in 7-base_geometry.py
# For the purpose of this self-contained immersive, BaseGeometry is defined here.
# In a typical Holberton environment, you would likely import it like this:
# from base_geometry import BaseGeometry

class BaseGeometry:
    """
    A base class for geometric shapes, providing common validation methods.
    """

    def area(self):
        """
        Calculates the area of the geometry.
        This method is not implemented in the base class and should be
        overridden by subclasses.

        Raises:
            Exception: Indicates that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value to ensure it is an integer greater than 0.

        Args:
            name (str): The name of the value being validated (e.g., "width", "height").
            value: The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
            width (int): The width of the rectangle. Must be a positive integer.
            height (int): The height of the rectangle. Must be a positive integer.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        # Validate width and height using the integer_validator from BaseGeometry
        # The validator will raise TypeError or ValueError if validation fails.
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Assign the validated values to private instance attributes
        self.__width = width
        self.__height = height
