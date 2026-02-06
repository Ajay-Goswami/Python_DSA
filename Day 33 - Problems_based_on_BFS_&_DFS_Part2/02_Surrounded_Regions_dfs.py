# Surrounded_Regions_dfs

# Capture surrounded regions using DFS – LeetCode 130

# Input: board = [["X","X","X"],["X","O","X"],["X","X","X"]]
# Output: [["X","X","X"],["X","X","X"],["X","X","X"]]  - Same board (center O becomes X)

def solve(board):  # O(m*n)
    if not board:
        return

    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if board[r][c] != 'O':
            return
        board[r][c] = '#'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for i in range(rows):
        dfs(i, 0)
        dfs(i, cols-1)

    for j in range(cols):
        dfs(0, j)
        dfs(rows-1, j)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == '#':
                board[r][c] = 'O'

    return board


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(solve(board))