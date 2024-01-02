#!/usr/bin/python3
"""returns a pascal triangle"""


def pascal_triangle(n):
    """
    returns a pascal triangle with integers
    """

    if n <= 0:

        return []
    pascal_triangle = [[1]]
    if n == 1:
        return pascal_triangle

    for row_num in range(1, n):
        l_index = -1
        r_index = 0
        c_row = []
        for col_num in range(row_num + 1):
            val = 0
            if l_index > -1:
                val += pascal_triangle[row_num - 1][l_index]
            if r_index < row_num:
                val += pascal_triangle[row_num - 1][r_index]
            l_index += 1
            r_index += 1
            c_row.append(val)
        pascal_triangle.append(c_row)
    return pascal_triangle
