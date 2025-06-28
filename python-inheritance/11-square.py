#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns:
            str: The string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """
        Returns a string representation of the Square instance,
        useful for debugging. Calls __str__.
        """
        return self.__str__()
