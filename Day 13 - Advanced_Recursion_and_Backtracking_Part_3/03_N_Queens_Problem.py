# N Queens Problem using Backtracking

# Input: Size of the chessboard (N)
# Output: All distinct solutions to the N-Queens puzzle

# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],
#          ["..Q.","Q...","...Q",".Q.."]]

def solveNQueens(n):
    result = []
    board = [["."] * n for _ in range(n)]
    def isSafe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == "Q":
                return False
        # Check left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        # Check right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

    # Backtracking function
    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if isSafe(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    backtrack(0)
    return result

n1 = 4
print(solveNQueens(n1))
