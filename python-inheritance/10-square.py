#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.

    A square is a special type of rectangle where all sides are equal.

    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): length of the square. Must be a positive integer.

        Raises:
            TypeError: If size is not an integer.
            """
        self.integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size
