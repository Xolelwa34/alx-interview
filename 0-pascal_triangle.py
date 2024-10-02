#!/usr/bin/python3
"""Returns a list of lists integers representing the 
Pascal's triangle of n"""


def pascal_triangle(n):
    """
    Method that creates a Pascal's triangle
    """
    new = []
    if n <= 0:
        return new
    new = [[1]]
    for i in range(1, n):
        arr = [1]
        for j in range(len(new[i - 1]) - 1):
            nums = new[i - 1]
            arr.append(new[i - 1][j] + new[i - 1][j + 1])
        arr.append(1)
        new.append(arr)
    return new


