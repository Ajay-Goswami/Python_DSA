# 04. Minimum Path Sum in Grid
# Dynamic Programming - 2D DP

# Problem: Given an m x n grid filled with non-negative numbers, find a path from
# top-left to bottom-right which minimizes the sum of all numbers along the path.
# You can only move either down or right at any point.

# Input: grid = [[1, 3, 1],
#                [1, 5, 1],
#                [4, 2, 1]]
# Output: 7

# Explanation: The path 1 -> 3 -> 1 -> 1 -> 1 = 7 is the minimum.
#   Path: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)
#   Other paths like 1 -> 1 -> 4 -> 2 -> 1 = 9 or 1 -> 1 -> 5 -> 2 -> 1 = 10
#   give higher sums.

# Time Complexity: O(m * n) | Space Complexity: O(n)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(m * n) | Space: O(m * n) for dp + O(m + n) recursion stack

def minPathSumMemo(i, j, grid, dp):
    if i == 0 and j == 0:
        return grid[0][0]

    if i < 0 or j < 0:
        return float('inf')

    if dp[i][j] != -1:
        return dp[i][j]

    up = grid[i][j] + minPathSumMemo(i - 1, j, grid, dp)
    left = grid[i][j] + minPathSumMemo(i, j - 1, grid, dp)

    dp[i][j] = min(up, left)
    return dp[i][j]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(m * n) | Space: O(m * n)

def minPathSumTabulation(m, n, grid):
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[0][0]
            else:
                up = grid[i][j] + dp[i - 1][j] if i > 0 else float('inf')
                left = grid[i][j] + dp[i][j - 1] if j > 0 else float('inf')
                dp[i][j] = min(up, left)

    return dp[m - 1][n - 1]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(m * n) | Space: O(n)

def minPathSum(m, n, grid):
    prev = [0] * n

    for i in range(m):
        curr = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                curr[j] = grid[0][0]
            else:
                up = grid[i][j] + prev[j] if i > 0 else float('inf')
                left = grid[i][j] + curr[j - 1] if j > 0 else float('inf')
                curr[j] = min(up, left)
        prev = curr

    return prev[n - 1]


grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]
m = len(grid)
n = len(grid[0])

# Memoization
dp = [[-1] * n for _ in range(m)]
print(f"Memoization: {minPathSumMemo(m - 1, n - 1, grid, dp)}")

# Tabulation
print(f"Tabulation: {minPathSumTabulation(m, n, grid)}")

# Space Optimized
print(f"Space Optimized: {minPathSum(m, n, grid)}")
