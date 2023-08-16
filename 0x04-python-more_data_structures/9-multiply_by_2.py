#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """multiplys everything by 2"""
    return ({mult: a_dictionary[mult] * 2 for mult in a_dictionary})
