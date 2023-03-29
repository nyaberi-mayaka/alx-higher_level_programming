#!/usr/bin/python3


"""
 A class Square that defines a square
"""


class Square:
    """
    class square reperesenting a square object
    """

    def __init__(self, size=0):
        """Class constructor"""
        self.size = size

    def area(self):
        """Calculates and returns the area of a square"""
        return (self.size ** 2)

    @property                # first decorate the getter method
    def size(self):
        """@size getter"""
        return (self.__size)

    @size.setter             # the property decorates with `.setter`
    def size(self, value):
        """Value size setter"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    """ rich comparison operators """
    def __lt__(self, other):
        """Defines the < comparison between Square objects."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison between Square objects."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Defines the == comparison between Square objects."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison between Square objects."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Defines the > comparison between Square objects."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison between Square objects."""
        return self.area() >= other.area()
