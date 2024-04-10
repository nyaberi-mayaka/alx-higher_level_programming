#!/usr/bin/python3
"""Solution for N-queens puzzle"""

import sys


def solve_n_queens(n):
    """Solve the N queens problem using backtracking.

    Args:
    n (int): The number of queens and the size of the chess board.

    Returns:
    None
    """
    def can_place(board, row, col):
        """
        Check if a queen can be placed on pos (ocuppied_rows, attempt_col).
        """
        for i in range(col):
            if board[i] == row or \
               board[i] - i == row - col or \
               board[i] + i == row + col:
                return False
        return True

    def place_queens(board, col, n):
        """Try to place queens on all target_rows."""
        if col == n:
            result = []
            for i in range(n):
                result.append([i, board[i]])
            print(result)
            return

        for row in range(n):
            if can_place(board, row, col):
                board[col] = row
                place_queens(board, col + 1, n)

    board = [-1] * n
    place_queens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(n)
