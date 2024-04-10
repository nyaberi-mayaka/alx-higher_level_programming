#!/usr/bin/python3

"""
a class Rectangle that defines a rectangle
"""


class Rectangle:
    """Defines a rectangle by width and height."""

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle instance.

        Args:
        width (int): width of the rectangle, defaults to 0.
        height (int): height of the rectangle, defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width of the rectangle.

        Args:
        value (int): width of the rectangle.

        Raises:
        TypeError: If width is not an integer.
        ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height of the rectangle.

        Args:
        value (int): height of the rectangle.

        Raises:
        TypeError: If height is not an integer.
        ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
