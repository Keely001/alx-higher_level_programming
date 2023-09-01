#!/usr/bin/python3
"""function to add two integers"""


def add_integer(a, b=98):
    """adds two integers
    Raises:
      raises if num is not int and float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))