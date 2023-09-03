#!/usr/bin/python3
"""a function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): string to check.
    Raise:
        text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip(" ")
    pos = 0
    while pos < len(text) and text[pos] == ' ':
        pos += 1
    while pos < len(text):
        print(text[pos], end="")
        if text[pos] == "\n" or text[pos] in ".?:":
            if text[pos] in ".?:":
                print("\n")
            pos += 1
            while pos < len(text) and text[pos] == ' ':
                pos += 1
            continue
        pos += 1
