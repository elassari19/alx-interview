#!/usr/bin/python3
""" Module Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ should rotate it 90 degrees """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """ invok function should rotate the matrix 90 degrees"""
    rotate_2d_matrix(matrix)
    print(matrix)
