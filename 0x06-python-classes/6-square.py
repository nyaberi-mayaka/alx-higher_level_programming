#!/usr/bin/python3


"""
 A class Square that defines a square
"""


class Square:
    """
    class square reperesenting a square object
    """

    def __init__(self, size=0, position=(0, 0)):
        """Class constructor"""
        self.size = size
        self.position = position

    def area(self):
        """Calculates and returns the area of a square"""
        return (self.size ** 2)

    @property                # first decorate the getter method
    def size(self):
        """@size getter"""
        return (self.__size)

    @property
    def position(self):
        """ @position getter"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """position setter"""

        if isinstance(value, tuple) or len(value) == 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int)\
           or value[0] < 0 or value[1] < 0:
            self.__position = value

        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
