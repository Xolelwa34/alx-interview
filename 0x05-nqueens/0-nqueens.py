#!/usr/bin/python3
"""
 Module to solve the nqueens 
"""
import sys


def backtrack(r, n, cols, positive, negative, board):
    """
    Solves the queens problem
    """
    if r == n:
        ret = []
        for l in range(len(board)):
            for j in range(len(board[l])):
                if board[l][j] == 1:
                    ret.append([l, j])
        print(ret)
        return

    for c in range(n):
        if c in cols or (r + c) in positive or (r - c) in negative:
            continue

        cols.add(c)
        positive.add(r + c)
        negative.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, positive, negative, board)

        cols.remove(c)
        positive.remove(r + c)
        negative.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Function to solve queens problem not to attack each other
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        List of lists in queens solutions
    """
    cols = set()
    positive_diag = set()
    negative_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, positive_diag, negative_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
