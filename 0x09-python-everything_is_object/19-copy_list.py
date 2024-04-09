#!/usr/bin/python3

"""a function that returns a copy of a list."""

def copy_list(l):
    """Returns a shallow copy of the input list.

    Args:
        l: The list to be copied.

    Returns:
        A new list containing a copy of the elements from the original list.

    This function uses slicing to create a new list with the same elements
    from the input list. Note that for nested mutable objects, this creates
    shallow copies, meaning the nested objects themselves are still shared
    references.
    """

    return l[:]
