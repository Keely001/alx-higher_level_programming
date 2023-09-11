#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle"""

    def __init__(self, size):
        """creates a new square.
        Args:
            size: size of the new square.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
