#!/usr/bin/python3
"""
a function that adds 2 integers
"""

def add_integer(a, b=98):
    """Adds two integers or floats, casting floats to integers.

    Args:
      a: The first number (int or float).
      b: The second number (int or float, default is 98).

    Raises:
      TypeError: If either a or b is not an integer or float.

    Returns:
      int: The sum of a and b, cast to an integer.
    """

    if a != a:
        a = 10.0
    if b != b:
        b = 10.0

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
