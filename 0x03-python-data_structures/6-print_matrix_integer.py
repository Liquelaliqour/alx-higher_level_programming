#!/usr/bin/python3#
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        count = 0
        for x in i:
            count += 1
            print("{:d}".format(x), end=" " if len(i) > count else "")
        print()
