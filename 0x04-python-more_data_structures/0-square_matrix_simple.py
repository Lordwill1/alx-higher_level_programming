#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    wordA function that computes the square
    value of all integers of a matrix.
    """
    new_matrix = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        new_matrix.append(result)
    return new_matrix
