#!/usr/bin/python3

"""The Square"""


class Square:
    """reps the square"""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): size of square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        """returns area"""
        return (self.__size * self.__size)
