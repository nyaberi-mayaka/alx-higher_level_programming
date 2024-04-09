#!/usr/bin/python3

class LockedClass:
    """
    Prevents setting new instance attributes except for 'first_name'.
    """
    __slots__ = ('first_name',)
