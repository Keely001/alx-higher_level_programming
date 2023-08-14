#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    state = []
    for x in my_list:
        if x % 2 == 0:
            state.append(True)
        else:
            state.append(False)
    return (state)
