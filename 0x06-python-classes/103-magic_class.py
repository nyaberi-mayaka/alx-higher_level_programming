#!/usr/bin/python3

import math
"""defines attribues of a circle"""


class MagicClass:
    """Represents a MagicClass object."""
    def __init__(self, radius=0):
        self.__radius = 0
        """Initializes an instance of a class"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Calculates and returns the area of a circle"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Calculates and returns the circumference of a circle"""
        return (2 * math.pi * self.__radius)
