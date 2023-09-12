#!/usr/bin/python3
"""function that writes to a text file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    args:
        filename:name of file
        text:text
    returns:
        the number of characters written"""
    chars_num = 0
    with open(filename, 'w', encoding='utf-8') as file:
        chars_num = file.write(text)
    return(chars_num)
