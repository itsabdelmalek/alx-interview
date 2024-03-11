#!/usr/bin/python3
"""
Prime Game Code
"""

def get_multiples(num, targ):
    """
    Finds multiples of a given number within a list
    """
    return [i for i in targ if i % num != 0]

def if_prime(i):
    """
    Check if a number is prime.
    """
    if i < 2:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

def get_primes(n):
    """
    Dispatch a given set into prime numbers and non-prime numbers.
    """
    primes = {i for i in n if if_prime(i)}
    return len(primes)

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

    for num in nums:
        cluster = set(range(1, num + 1))
        temp = get_primes(cluster)

        if temp % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
