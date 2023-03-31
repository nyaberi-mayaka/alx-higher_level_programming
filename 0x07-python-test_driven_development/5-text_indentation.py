#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters
    `.`, `?`, `:`
    Raises a TypeError if text is no a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    lines = ".?:"

    for i in range(len(text)):
        if text[i] == " " and text[i - 1] in lines:
            print("{}".format(""), end="")
        else:
            print("{}".format(text[i]), end="")
        if text[i] in lines:
            print("{}".format("\n"))
