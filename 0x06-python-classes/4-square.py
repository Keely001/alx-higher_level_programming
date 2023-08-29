#!/usr/bin/python3
"""The Square"""


class Square:
    """reps the square"""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): size of square.
        """
        self.size = size
        
    @property
    def size(self):
        """set size"""
        return(self.__size)
    @size.setter
    def size(self,value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """returns area"""
        return (self.__size * self.__size)
