#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        x = list(a_dictionary.values())[0]
        for i, v in a_dictionary.items():
            if v > x:
                x, y = v, i
        return (y)
    else:
        return (None)
