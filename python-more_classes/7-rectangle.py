#!/usr/bin/python3
"""
This module defines the Rectangle class, demonstrating encapsulation
with private instance attributes and pros for width and height validation.

It provides a robust way to define rectangles, ensuring their dimensions
are always valid integers through controlled access via getters and setters.
"""


class Rectangle:
    """
    Represents a rectangle with controlled width and height access.

    This class defines a rectangle by its width and height, ensuring that
    both dimensions are always non-negative integers. Both width and height
    are stored as private instance attributes to enforce strict control
    over their types and values.

    Attributes:
        __width (int): The width of the rectangle. It's stored as a private
                       attribute to enforce type and value constraints, and its
                       value is accessed/modified via properties.
        __height (int): The height of the rectangle. It's stored as a private
                        attribute to force type and value constraints, and its
                        value is accessed/modified via properties.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with validation for dimensions.

        This constructor sets the initial width and height of the rectangle.
        It leverages the `width` and `height` properties' setter methods
        to perform rigorous checks, ensuring that both dimensions are
        integers and non-negative.

        Args:
            width (int, optional): The width of the rectangle.
                                   Defaults to 0 if not provided.
            height (int, optional): The height of the rectangle.
                                    Defaults to 0 if not provided.

        Raises:
            TypeError: If `width` or `height` is not an integer.
            ValueError: If `width` or `height` is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: Retrieves the width of the rectangle.

        This property acts as a getter for the private instance attribute
        `__width`. It allows controlled access to the width value.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation.

        This property acts as a setter for the private instance attribute
        `__width`. It performs rigorous checks to ensure that the assigned
        `value` is an integer and non-negative.

        Args:
            value (int): The new width for the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: Retrieves the height of the rectangle.

        This property acts as a getter for the private instance attribute
        `__height`. It allows controlled access to the height value.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation.

        This property acts as a setter for the private instance attribute
        `__height`. It performs rigorous checks to ensure that the assigned
        `value` is an integer and non-negative.

        Args:
            value (int): The new height for the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([Rectangle.print_symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
