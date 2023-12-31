#!/usr/bin/python3
"""function that appends text to a file"""


def append_write(filename="", text=""):
    """function that appends text to a file
    args:
        filename:name of file
        text:text to append
    returns:
        the number of characters appended"""
    chars_num = 0
    with open(filename, 'a', encoding='utf-8') as file:
        chars_num = file.write(text)
    return(chars_num)
