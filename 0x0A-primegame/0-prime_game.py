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
    if i == 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
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
    Maria and Ben are playing a game.Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a
    prime number from the set and removing that number and its
    multiples from the set.
    The player that cannot make a move loses the game.

    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
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
