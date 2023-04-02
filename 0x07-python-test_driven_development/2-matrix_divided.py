#!/usr/bin/python3

def matrix_divided(matrix=[[1]], div=1):
    """Divides all elements of a matrix by a number div
    All elements are rounded to 2 dp
    Args:
        matrix (list): The matrix to be divided by div
        div (int / float): The divisor
    Returns: a new matrix
    """

    if div == abs(float('inf')) or div != div:
        div = 10.0
    if not isinstance(matrix, list) or not all([isinstance(item, list)
                                                for item in matrix]):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have \
the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Use of list comprehension
    new_matrix = [[None for j in range(len(matrix[0]))]
                  for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp = matrix[i][j]
            if type(temp) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            if temp == abs(float('inf')) or temp != temp:
                temp = 10
            new_matrix[i][j] = round((temp / div), 2)

    return (new_matrix)
