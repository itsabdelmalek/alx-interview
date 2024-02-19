#!/usr/bin/python3
"""
 Script to Rotate a 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place
    """
    size = len(matrix)
    for layer in range(size // 2):
        first, last, offset = layer, size - 1 - layer, 0
        for i in range(first, last):
            top_element = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top_element
            offset += 1
