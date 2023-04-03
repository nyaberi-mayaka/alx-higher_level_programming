#!/usr/bin/python3

"""Class Rectangle that defines a rectangle
"""


class Rectangle:
    """Class Rectangle that represents a rectangle object
    """
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object with the given width and
           height.
        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute of the Rectangle object"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter method for the width attribute of the Rectangle object"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute of the Rectangle object"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method for the height attribute of the Rectangle object"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns:
            The area of the rectangle (width times height).
        """
        return (self.width * self.height)

    def perimeter(self):
        """Returns:
            The perimeter of the rectangle 2 times (width plus height).
        """
        return (2 * (self.width + self.height))
