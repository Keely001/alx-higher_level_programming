#!/usr/bin/python3
"""a function that adds a new attribute to an object if it’s possible:"""


def add_attribute(obj, att, value):
    """adds a new attribute to the object if possible.

    Args:
        obj (any): object to add
        att (str): name of the attribute
        value (any): value of attribute
    Raises:
        TypeError: If attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
    