#!/usr/bin/python3
"""a function that inserts a line of text to a file,
after each line containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file,
    after each line containing a specific string
    Args:
        filename (str): file name
        search_string (str): string to look for
        new_string (str): inserted string
    """
    txt = ""
    with open(filename) as f:
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as f:
        f.write(txt)
