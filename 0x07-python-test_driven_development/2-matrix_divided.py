#!/usr/bin/python3

def matrix_divided(matrix, div):

    if not isinstance(matrix, list) or not all([isinstance(item, list)
                                                for item in matrix]):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    new_matrix = [[None for j in range(len(matrix[0]))]
                  for i in range(len(matrix))]

    for i in range(len(matrix)):
        l = len(matrix[0])
        for j in range(len(matrix[i])):
            if len(matrix[i]) != l:
                   raise TypeError("Each row of the matrix must have \
the same size")
            if not isinstance(div, int) and not isinstance(div, float):
                raise TypeError("div must be a number")

            if div == 0:
                raise ZeroDivisionError("division by zero")
            new_matrix[i][j] = round(matrix[i][j] / div, 2)

    return (new_matrix)
