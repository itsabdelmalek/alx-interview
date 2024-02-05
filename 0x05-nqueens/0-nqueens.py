#!/usr/bin/python3
"""
N queens code
"""

import sys


def solve_nqueens(n):
    """
    Main function to solve the N-Queens problem for a given value of N.
    """
    if n == 0:
        return [[]]

    temp_solution = solve_nqueens(n - 1)

    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in temp_solution
            if is_safe_queen((n, i + 1), solution)]


def is_attack(sqre, queen):
    """
    Check if two queens can attack each other.
    """
    (r1, c1) = sqre
    (r2, c2) = queen
    return (r1 == r2) or (c1 == c2) or abs(r1 - r2) == abs(c1 - c2)


def is_safe_queen(sqr, queens):
    """
    Check if a given square is safe from attack by any queens.
    """
    for queen in queens:
        if is_attack(sqr, queen):
            return False
    return True


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    n_q = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)

if n_q < 4:
    print('N must be at least 4')
    sys.exit(1)

for answer in reversed(solve_nqueens(n_q)):
    result = [[i - 1 for i in p] for p in map(list, answer)]
    print(result)
