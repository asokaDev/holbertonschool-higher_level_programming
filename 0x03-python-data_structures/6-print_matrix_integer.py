#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < len(matrix[j]) - 1:
                print("{:d}".format(matrix[j][i]), end=" ")
            else:
                print("{:d}".format(matrix[j][i]), end="")
        print("")
