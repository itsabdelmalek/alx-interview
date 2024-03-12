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
    Count = 0
    for i in range(2, n + 1):
        if if_Prime(i):
            Count += 1
    return Count


def isWinner(x, nums):
    """
    determine who the winner of each game is.
    """

    players = {'Maria': 0, 'Ben': 0}
    cluster = set()
    for elem in range(x):
        nums.sort()
        num = nums[elem]
        for i in range(1, num + 1):
            cluster.add(i)
            if i == num + 1:
                break
        temp = get_Primes(cluster)

        if temp % 2 == 0:
            players['Ben'] += 1
        elif temp % 2 != 0:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
