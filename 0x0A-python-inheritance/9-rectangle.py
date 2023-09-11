#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """creates a rectangle
        Args:
            width : width
            height : height
        Return:
            None
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        
        
        def __str__(self):
            """print() should print, and str() should return,
            the following rectangle description"""
            string = "[" + str(self.__class__.__name__) + "] "
            string += str(self.__width) + "/" + str(self.__height)
            return string
        
        def area(self):
            """Returns the area"""
            return self.__width * self.__height