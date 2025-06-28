#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
            height (int): The height of the rectangle. Must be a positive.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Assign the validated values to private instance attributes
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        The format is: [Rectangle] <width>/<height>.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    # __repr__ is often implemented for debugging, and by default,
    # if __str__ is defined but __repr__ is not, print() uses __str__.
    # However, explicitly defining __repr__ to call __str__ is good practice
    # if you want the same representation for both.
    def __repr__(self):
        """
        Returns a string representation of the Rectangle instance,
        useful for debugging. Calls __str__.
        """
        return self.__str__()
