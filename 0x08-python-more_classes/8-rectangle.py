#!/usr/bin/python3

"""Class Rectangle that defines a rectangle
"""


class Rectangle:
    """Class Rectangle that represents a rectangle object
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object with the given width and
           height.
        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.width + self.height))

    def __str__(self):
        """Returns a string representation of the Rectangle object.
           The string is a rectangle made of '#' characters with the
           same width and height as the object.
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return (string)

        for i in range(self.height):
            for j in range(self.width):
                string += f'{self.print_symbol}'
            if i < self.height - 1:
                string += '\n'
        return (string)

    def __repr__(self):
        """Returns a string representation of the Rectangle object that
        can be used to recreate it.

        Returns:
            str: A string that includes the class name, width, and height
            of the Rectangle object.
        """
        class_name = type(self).__name__
        return f"{class_name}({self.width}, {self.height})"

    def __del__(self):
        """Destructor for the Rectangle object.
        Prints a message to indicate that the object is being deleted.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the one with the greater
           area.
        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.
        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of
            Rectangle.
        Returns:
            The rectangle with the greater area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
