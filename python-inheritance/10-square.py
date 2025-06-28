#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from BaseGeometry.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    def __init__(self, size):
        """
        Initializes a new Rectangle instance.

        Args:
            size (int): The width of the rectangle. Must be a positive.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("size", width)

        super().__init__(size, size)
        # Assign the validated values to private instance attributes
        self.__size = size
