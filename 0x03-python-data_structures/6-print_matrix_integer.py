#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        x = len(matrix[i])
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j < x - 1:
                print("{:s}".format(" "), end="")
        print()
