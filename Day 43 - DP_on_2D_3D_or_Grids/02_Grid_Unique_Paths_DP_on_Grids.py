# 02. Grid Unique Paths (DP on Grids)
# Dynamic Programming - 2D DP

# Problem: You are given an m x n grid. A robot is placed at the top-left corner (0, 0).
# The robot can only move either down or right at any point. Find the number of unique
# paths the robot can take to reach the bottom-right corner (m-1, n-1).

# Input: m = 3, n = 7
# Output: 28

# Explanation: From (0,0) to (2,6), the robot needs to make exactly 2 down moves
#   and 6 right moves in some order. Total unique orderings = C(8,2) = 28.
#   But we solve it using DP here to understand the grid DP pattern.

# Time Complexity: O(m * n) | Space Complexity: O(n)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(m * n) | Space: O(m * n) for dp + O(m + n) recursion stack

def uniquePathsMemo(i, j, dp):
    if i == 0 and j == 0:
        return 1

    if i < 0 or j < 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    up = uniquePathsMemo(i - 1, j, dp)
    left = uniquePathsMemo(i, j - 1, dp)

    dp[i][j] = up + left
    return dp[i][j]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(m * n) | Space: O(m * n)

def uniquePathsTabulation(m, n):
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                up = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = up + left

    return dp[m - 1][n - 1]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(m * n) | Space: O(n)

def uniquePaths(m, n):
    prev = [0] * n

    for i in range(m):
        curr = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                curr[j] = 1
            else:
                up = prev[j] if i > 0 else 0
                left = curr[j - 1] if j > 0 else 0
                curr[j] = up + left
        prev = curr

    return prev[n - 1]


m = 3
n = 7

# Memoization
dp = [[-1] * n for _ in range(m)]
print(f"Memoization: {uniquePathsMemo(m - 1, n - 1, dp)}")

# Tabulation
print(f"Tabulation: {uniquePathsTabulation(m, n)}")

# Space Optimized
print(f"Space Optimized: {uniquePaths(m, n)}")
