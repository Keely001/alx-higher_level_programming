#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints key and value"""
    [print("{}: {}".format(i, a_dictionary[i])) for i in sorted(a_dictionary)]
