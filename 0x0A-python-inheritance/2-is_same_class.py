#!/usr/bin/python3
"""a function that returns True if the object is exactly """


def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly
    Args:
        obj (any): object
        a_class (type): The class.
    Returns:
       true if same , else false
    """
    if type(obj) == a_class:
        return True
    return False