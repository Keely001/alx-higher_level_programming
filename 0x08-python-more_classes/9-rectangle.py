#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by:
    (based on 4-rectangle.py)"""


class Rectangle:
    """a class Rectangle that defines a rectangle by:
        (based on 4-rectangle.py)"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle.
        Args:
            width (int): The width of rectangle.
            height (int): The height of rectangle.
        """

        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
    
    def __str__(self) -> str:
        """print the rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for a in range(self.__height):
            for b in range(self.__width):
                rect.append(str(self.print_symbol))
            if a != self.__height - 1:
                rect.append("\n")
        return("".join(rect))

    def __repr__(self):
        """return a string rep of the rectangle"""
        ret = "Rectangle(" + str(self.__width)
        ret += ", " + str(self.__height) + ")"
        return(ret)

    def __del__(self):
        """message for deletion and decrement of instances"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns rect with  the bigger area
        Arguments:
            rect_1 (Rectangle): first rectangle.
            rect_2 (Rectangle): second rectangle.
        Raises:
            TypeError: if one of them are not rectangles.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)

        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns a square
        Args:
            size (int): width and height of square
        """
        return (cls(size, size))
    