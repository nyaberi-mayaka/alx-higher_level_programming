#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """Prints a message with the provided first and last name.

    Args:
      first_name: A string representing the first name. (required)
      last_name: A string representing the last name. (optional, defaults to "")

    Raises:
      TypeError: If either first_name or last_name is not a string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    """
    full_name = f"{first_name.strip()} {' '.join([ln.strip() for ln in last_name.split()])}"

    if not full_name:
        raise TypeError("first_name must be a string")
    """

    print("My name is {0} {1}".format(first_name, last_name))
