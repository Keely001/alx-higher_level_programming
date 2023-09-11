#!/usr/bin/python3
"""a function that returns True if the object is an instance """


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is exactly
    Args:
        obj (any): object
        a_class (type): The class.
    Return:
       true if same , else false
       
    """
    if isinstance(obj, a_class):
        return True
    return False
