#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if not i:
            print()
            continue
        print(" ".join("{:d}".format(num) for num in i))
