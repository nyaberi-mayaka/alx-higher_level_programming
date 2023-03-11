#!/usr/bin/python3
def no_c(my_string):
    strs = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            strs += char
    return (strs)
