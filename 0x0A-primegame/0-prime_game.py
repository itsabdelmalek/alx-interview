#!/usr/bin/python3
"""Prime game code"""


def if_Prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_Prime(num):
    """gets the prime numbers in a list."""
    count = 0
    for num in num:
        if if_Prime(num):
            count += 1
    return count


def isWinner(x, nums):
    """Determines who the winner of the game is."""
    ben = 0
    maria = 0
    if x <= 0 or not nums:
        return None
    for num in range(x):
        num_arr = [n for n in range(1, nums[num] + 1)]
        if get_Prime(num_arr) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if ben == maria:
        return None
    return "Maria"
