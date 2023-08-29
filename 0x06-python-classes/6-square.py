#!/usr/bin/python3
"""The Square"""


class Square:
    """reps the square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size (int): size of square.
        """
        self.size = size
        self.position = position
        
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
        
    @property
    def position(self):
        """set current position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
    def area(self):
        """returns area"""
        return (self.__size * self.__size)
    def my_print(self):
        """prints square using #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")