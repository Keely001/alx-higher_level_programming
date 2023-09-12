#!/usr/bin/python3
"""defines a student"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """init the student
        Args:
            first_name (str):first name
            last_name (str):last name
            age (int):age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            result = {m: getattr(self, m) for m in attrs if hasattr(self, m)}
            return(result)
        return self.__dict__
