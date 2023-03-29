#!/usr/bin/python3

"""defines attribues of a circle"""


class MagicClass:
    def __init__(self, radius=0):
        """Initializes an instance of a class"""
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Calculates the area of a circle"""
        return (pi * self.__radius ** 2)

    def circumference(self):
        """Calculates the circumference of a circle"""
        return (2 * pi * self.__radius)
