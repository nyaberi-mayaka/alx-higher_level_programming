#!/usr/bin/python3

def say_my_name(first_name="", last_name=""):
    """Prints the first and last name
    Checks if both are strings and raises corresponding Exceptions
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {0} {1}".format(first_name, last_name))
