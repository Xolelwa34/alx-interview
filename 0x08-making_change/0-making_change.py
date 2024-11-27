#!/usr/bin/python3
"""
Module to make changes
"""


def makeChange(coins, total):
    """
      Creates change for total

    Args:
        coins ([List]): [List of Coins available]
        total ([int]): [total amount needed]
    """
    if total <= 0:
        return 0
    check = 0
    ret = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            ret += 1
        if check == total:
            return ret
        check -= i
        ret -= 1 
    return -1
