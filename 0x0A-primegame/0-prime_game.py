#!/usr/bin/python3
"""
Prime Game code
"""

def isWinner(x, nums):
    """
    Function to determine the winner of a game played between Maria and Ben.
    
    Parameters:
    x (int): The number of rounds.
    nums : List of integers representing the maximum number for each round.

    Returns:
    str: The name of the player who won the most rounds.
    """

    def sieve(n):
        """
        Function to generate all primes up to n using the Sieve algorithm.
        
        Parameters:
        n (int): The upper limit for generating prime numbers.

        Returns:
        list: A boolean list where True indicates the index is a prime number.
        """
        primes = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (primes[p] == True):
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        return primes

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve(n)
        prime_count = sum(primes) - 2
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
