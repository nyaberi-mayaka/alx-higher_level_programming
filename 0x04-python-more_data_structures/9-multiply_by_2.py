#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if isinstance(a_dictionary, dict):
        return ({i: v * 2 for i, v in a_dictionary.items()})
