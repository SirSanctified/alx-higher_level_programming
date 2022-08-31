#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list([list(map(lambda x: x * x, [i for i in j])) for j in matrix])
