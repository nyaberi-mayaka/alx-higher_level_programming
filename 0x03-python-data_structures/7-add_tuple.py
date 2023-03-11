#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lst = [[] for i in range(2)]
    for i in range(2):
        if len(tuple_a) < i + 1:
            x = 0
        else:
            x = tuple_a[i]

        if len(tuple_b) < i + 1:
            y = 0
        else:
            y = tuple_b[i]

        lst[i] = x + y
    tp = (lst[0], lst[1])
    return (tp)
