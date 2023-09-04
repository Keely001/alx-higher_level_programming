#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)"""


class Rectangle:
    """a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle.
        Args:
            width (int): The width of rectangle.
            height (int): The height of rectangle.
        """
        
        self.height = height
        self.width = width

    @property
    def width(self):
        """set new width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set new height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """returns area of rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return(0)
        return((self.width * 2) + (self.height * 2))