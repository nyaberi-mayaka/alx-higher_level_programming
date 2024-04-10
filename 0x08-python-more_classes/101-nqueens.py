#!/usr/bin/python3
"""Solution for N-queens puzzle"""

import sys


def solve_n_queens(n):
    """Solve the N queens problem using backtracking."""

    def can_place(board, row, col):
        """Check if a queen can be placed on board at (row, col)."""
        for i in range(col):
            if (board[i] == row or
                    board[i] - i == row - col or
                    board[i] + i == row + col):
                return False
        return True

    def place_queens(board, col, n):
        """Place queens on the board."""
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


def main():
    """Main function to check arguments and solve the problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
