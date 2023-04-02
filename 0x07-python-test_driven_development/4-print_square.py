#!/usr/bin/python3

def print_square(size):
    """Prints a square with the character #
    Checks for logical and Type errors and raises the corresponding Exceptions

    Args:
        size (int): The length of the square
            Must be an integer greater or equal to zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print(size * "#")