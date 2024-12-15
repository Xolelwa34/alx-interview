#!/usr/bin/python3
"""main func"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing n for each round.

    Returns:
        str: Name of the player witt wins ("Maria" or "Ben"), or None if tied.
    """
    if x < 1 or not nums:
        return None

    # Find the maximum value of n in nums to calculate primes up to that point
    max_n = max(nums)

    # Step 1: Use Sieve of Eratosthenes to determine prime numbers up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Step 2: Precompute the number of primes up to each index
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Step 3: Simulate the game for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
