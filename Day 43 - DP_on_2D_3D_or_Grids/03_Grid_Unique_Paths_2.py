# 03. Grid Unique Paths 2 (with Obstacles)
# Dynamic Programming - 2D DP

# Problem: You are given an m x n grid with obstacles. An obstacle is marked as 1 and
# free space is marked as 0. A robot starts at the top-left corner and wants to reach
# the bottom-right corner. The robot can only move down or right. Find the number of
# unique paths considering obstacles.

# Input: grid = [[0, 0, 0],
#                [0, 1, 0],
#                [0, 0, 0]]
# Output: 2

# Explanation: There's one obstacle in the middle at (1,1).
#   Path 1: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)
#   Path 2: (0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2)
#   The path through (1,1) is blocked so only 2 paths exist.

# Time Complexity: O(m * n) | Space Complexity: O(n)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(m * n) | Space: O(m * n) for dp + O(m + n) recursion stack

def uniquePaths2Memo(i, j, grid, dp):
    if i >= 0 and j >= 0 and grid[i][j] == 1:
        return 0

    if i == 0 and j == 0:
        return 1

    if i < 0 or j < 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    up = uniquePaths2Memo(i - 1, j, grid, dp)
    left = uniquePaths2Memo(i, j - 1, grid, dp)

    dp[i][j] = up + left
    return dp[i][j]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(m * n) | Space: O(m * n)

def uniquePaths2Tabulation(m, n, grid):
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[i][j] = 1
            else:
                up = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = up + left

    return dp[m - 1][n - 1]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(m * n) | Space: O(n)

def uniquePaths2(m, n, grid):
    prev = [0] * n

    for i in range(m):
        curr = [0] * n
        for j in range(n):
            if grid[i][j] == 1:
                curr[j] = 0
            elif i == 0 and j == 0:
                curr[j] = 1
            else:
                up = prev[j] if i > 0 else 0
                left = curr[j - 1] if j > 0 else 0
                curr[j] = up + left
        prev = curr

    return prev[n - 1]


grid = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
m = len(grid)
n = len(grid[0])

# Memoization
dp = [[-1] * n for _ in range(m)]
print(f"Memoization: {uniquePaths2Memo(m - 1, n - 1, grid, dp)}")

# Tabulation
print(f"Tabulation: {uniquePaths2Tabulation(m, n, grid)}")

# Space Optimized
print(f"Space Optimized: {uniquePaths2(m, n, grid)}")
