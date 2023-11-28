import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at a given position.

    Args:
        board (list): The chessboard representation.
        row (int): The current row.
        col (int): The current column.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A list of all solutions to the N Queens problem.
    """
    def solve(board, row, n, solutions):
        if row == n:
            solutions.append([[i, board[i].index('Q')] for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'
                solve(board, row + 1, n, solutions)
                board[row][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(board, 0, n, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
