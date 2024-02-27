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
    dp = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
