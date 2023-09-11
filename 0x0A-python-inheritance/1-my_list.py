#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """class that inherits a list class"""

    def print_sorted(self):
        """prints a list in an ascending order"""
        print(sorted(self))