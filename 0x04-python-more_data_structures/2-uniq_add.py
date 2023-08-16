#!/usr/bin/python3
def uniq_add(my_list=[]):
    nums = set(my_list)
    total = 0
    for num in nums:
        total += num
    return total
