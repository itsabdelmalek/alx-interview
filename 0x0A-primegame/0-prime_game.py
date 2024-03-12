#!/usr/bin/python3
"""
Prime Game code
"""


def get_Multiples(num, mult):
    """
    Finds multiples of a given number within a list
    """
    for i in mult:
        if i % num == 0:
            mult.remove(i)
    return mult


def if_Prime(i):
    """
    Checks if a number is prime.
    """
    if (i <= 1):
        return False
    j = 2
    while (j * j) <= i:
        if (i % j) == 0:
            return False
        j += 1
    return True


def get_Primes(n):
    """
    Dispatchs a given set into prime numbers and non-prime numbers.
    """
    count = 0
    targ = list(n)
    for i in range(1, len(targ) + 1):
        if if_Prime(i):
            count += 1
            targ.remove(i)
            targ = get_Multiples(i, targ)
        else:
            pass
    return count


def isWinner(x, nums):
    """
    determine who the winner of each game is.
    """

    ben_wins = maria_wins = 0

    if x <= 0:
        return None

    for i in range(x):
        if get_Primes(nums[i]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins == maria_wins:
        return None
    return 'Ben' if ben_wins > maria_wins else 'Maria'
