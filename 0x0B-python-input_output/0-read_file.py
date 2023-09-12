#!/usr/bin/python3
"""a function that reads a text file """


def read_file(filename=""):
    """a function that reads a text file
    args:
        filename: name of file"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
