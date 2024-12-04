#!/usr/bin/python3
"""
Module for Islad perimeter function
"""


def island_perimeter(grid):
    """Returns the Island perimiter
     grid represents water by 0 and land by 1.
    Args:
     Grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    rows = len(grid[0])
    cols = len(grid)
    ram = 0
    size = 0

    for i in range(cols):
        for j in range(rows):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                ram += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    ram += 1
    return size * 4 - ram * 2

