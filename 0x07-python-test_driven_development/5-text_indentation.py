#!/usr/bin/python3

"""
a function that prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with two new lines after ., ?, and : characters.

    Args:
     text: A string representing the text to be indented.

    Raises:
     TypeError: If text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    words = text.split()

    for i, word in enumerate(words):
        print(word.rstrip(), end="")

        if word.endswith((".", "?", ":")):
            print("\n\n", end="")

        else:
            if i != len(words) - 1:
                print(" ", end="")
    """
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
    """
