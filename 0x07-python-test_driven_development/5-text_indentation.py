#!/usr/bin/python3
""" function that prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters
    `.`, `?`, `:`
    Raises a TypeError if text is no a string
    There should be no space at the beginning or at the end of each
    printed line
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    lines = ".?:"

    i = 0
    while i < len(text) and text[i] == " ":
        i += 1
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] == "\n" or text[i] in lines:
            if text[i] in lines:
                print("{}".format("\n"))
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
