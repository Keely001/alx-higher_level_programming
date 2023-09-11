#!/usr/bin/python3
""" an empty class base geometry"""


class BaseGeometry:
    """an empty class"""
    
    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ensures its an int
        Args:
            name: name of parameter
            value: its value
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
