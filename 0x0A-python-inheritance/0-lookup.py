#!/usr/bin/python3
"""a function that returns the list of available attributes"""


def lookup(obj):
    """returns obj available attributes"""
    return (dir(obj))