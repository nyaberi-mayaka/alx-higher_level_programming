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

        if isinstance(value, tuple) and len(value) == 2 and \
           isinstance(value[0], int) and isinstance(value[1], int)\
           and value[0] >= 0 and value[1] >= 0:
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

    def __str__(self):
        """Returns the string representation of a square."""
        string = ""
        if self.__size == 0:
            return ""
        else:
            string += "\n" * self.__position[1]

            for i in range(self.__size):
                string += " " * self.__position[0]
                string += "#" * self.__size
                if i != self.__size - 1:
                    string += "\n"
            return (string)
