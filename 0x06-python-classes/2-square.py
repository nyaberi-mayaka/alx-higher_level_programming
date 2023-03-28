#!/usr/bin/python3


"""
 A class Square that defines a square
"""


class Square:
    """
    class square reperesenting a square object
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
