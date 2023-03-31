#!/usr/bin/python3

def add_integer(a, b=98):
    """Takes two arguments and adds them.
    Args:
        a (int): The first parameter.
        b (int): The second parameter
    Returns:
        a + b.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return (a + b)
