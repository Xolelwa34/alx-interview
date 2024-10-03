#!/usr/bin/python3
"""
Creates a list lists of integers representing Pascal's Triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
