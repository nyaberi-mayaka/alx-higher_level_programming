#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        for i in my_list:
            if j < x:
                print("{}".format(i), end="")
                j += 1

                """            else:
                raise IndexExceeds
                """
    except Exception as e:
        print()
    else:
        print()

    return (j)


""""
class IndexExceeds(Exception):
    pass
"""
