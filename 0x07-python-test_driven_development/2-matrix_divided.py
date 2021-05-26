#!/usr/bin/python3
def matrix_divided(matrix, div):
    """''def matrix_divided(matrix, div):'' divide each
    elelemt of the matrix is divided by div and
    return a new matrix """

    if type(div) not in [int, float]:
        raise TypeError("return a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError(
            "return(list of lists) of \
        integers/floats"
        )
    else:

        for i in matrix:
            if type(i) is not list:
                raise TypeError(
                    "return(list of lists) of \
                integers/floats"
                )
            else:
                for j in i:
                    if type(j) not in [int, float]:
                        raise TypeError(
                            "return (list of lists) \
                        of integers/floats"
                        )

        r_len = len(matrix[0])
        for n in range(len(matrix)):
            if len(matrix[n]) != r_len:
                raise TypeError(
                    "each matrix must have de same size"
                )

        New_matrix = [[round((el / div), 2) for el in i] for i in matrix]

    return New_matrix
