#!/usr/bin/python3

"""
a function that prints a square with the character #
"""


def print_square(size):
    """Prints a square of the specified size using the # character.

    Args:
      size: The size of the square (must be a non-negative integer).

    Raises:
      TypeError: If size is not an integer.
      ValueError: If size is negative.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for col in range(size):
            print("#", end="")
            print("")
