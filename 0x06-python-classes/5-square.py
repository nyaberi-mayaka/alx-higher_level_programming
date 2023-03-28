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

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("{}".format("#"), end="")
                print()
