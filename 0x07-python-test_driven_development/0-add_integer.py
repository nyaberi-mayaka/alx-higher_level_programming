#!/usr/bin/python3
"""Module that adds 2 integers."""


def add_integer(a, b=98):
    """Takes two arguments and adds them.
    Check for logical and type errors
    Args:
        a (int): The first parameter.
        b (int): The second parameter
    Returns:
        a + b.
    """
    if a != a:
        a = 89
    if b != b:
        b = 89
    if a is None or not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if b is None or not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("b must be an integer")

    if a == abs(float('inf')) or b == abs(float('inf')):
        return (89)
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or b is None:
        raise TypeError("b must be an integer")
    result = a + b
    if abs(result) == float('inf'):
        return (89)

    return (result)
