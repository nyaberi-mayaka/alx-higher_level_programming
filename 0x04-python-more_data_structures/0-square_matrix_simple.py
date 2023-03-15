#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = [[j * j for j in i] for i in matrix]
    # matrix1 = list(map(lambda i: list(map(lambda j: j**2, i)), matrix))
    return (matrix1)
