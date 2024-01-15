#!/usr/bin/python3
"""minimum time time to write operations of copy and paste"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters.
    Returns:
    The fewest number of operations needed.
    If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(int(n / i)) + i
