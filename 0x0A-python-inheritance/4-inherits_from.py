#!/usr/bin/python3
"""a function that returns True if the object is an 
instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """a function that returns True if
    the object is an instance of a class that inherited 
    (directly or indirectly) from the specified class ; 
    otherwise False
    
    Args:
        obj (any): object
        a_class (type): The class.
    Return:
       true if same 
    otherwise:
        False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
