import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at a given position.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row of the position to check.
        col (int): The column of the position to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(len(board)):
        if board[row][i] == "Q" or board[i][col] == "Q":
            return False

    for i in range(len(board)):
        for j in range(len(board)):
            if (i + j == row + col or i - j == row - col) and board[i][j] == "Q":
                return False

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem using backtracking.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A list of all solutions to the N Queens problem.
    """
    def solve(board, col):
        if col == n:
            solutions.append([board[i][:] for i in range(n)])
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = "Q"
                solve(board, col + 1)
                board[i][col] = "."

    solutions = []
    chessboard = [["." for _ in range(n)] for _ in range(n)]
    solve(chessboard, 0)
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
