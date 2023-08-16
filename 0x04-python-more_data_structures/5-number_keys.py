#!/usr/bin/python3
def number_keys(a_dictionary):
    sum = 0
    keys = list(a_dictionary.keys())
    for i in keys:
        sum += 1
    return sum
