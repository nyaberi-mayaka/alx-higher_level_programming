#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        x = list(a_dictionary.values())[0]
        y = ""
        for i, v in a_dictionary.items():
            if v >= x:
                x = v
                y = i
    return (y)
