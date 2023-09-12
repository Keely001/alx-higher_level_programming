#!/usr/bin/python3
""" returns a list of lists of integers representing
the Pascal’s triangle of """


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of """
    if n <= 0:
        return []
    tringle_array = [[1]]
    while len(tringle_array) != n:
        arr = [1]
        a = tringle_array[-1]

        for x in range(len(a) - 1):
            arr.append(a[x] + a[x + 1])
        arr.append(1)
        tringle_array.append(arr)
    return (tringle_array)
