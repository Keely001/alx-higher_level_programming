#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """new Rectangle.

        Args:
            width (int): width
            height (int): height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """returns readable info"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
