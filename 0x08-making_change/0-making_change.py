#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    return: Fewest number of coins needed to meet the total
             -1 if total is not achievable with the given coins
             0 if total is 0 or less
    """

    if total <= 0:
        return 0
    coins.sort(reverse=True)

    num_coins = 0
    remaining_total = total

    for coin in coins:
        if coin <= remaining_total:
            num_coins += remaining_total // coin
            remaining_total %= coin

    return num_coins if remaining_total == 0 else -1
