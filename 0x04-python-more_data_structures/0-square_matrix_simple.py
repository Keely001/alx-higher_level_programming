#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for row in range(len(matrix)):
        new_matrix[row] = list(map(lambda x: x*x, matrix[row]))
    return (new_matrix)
