#!/usr/bin/python3
"""a function that prints a square with the character #"""


def print_square(size):
    """ prints a square
    Args:
        size (int): size of square

    Raises:
        TypeError:when not an int 
        ValueError: when less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
        
        
        
