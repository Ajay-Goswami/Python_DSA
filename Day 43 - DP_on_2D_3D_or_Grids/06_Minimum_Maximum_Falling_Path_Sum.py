# 06. Minimum / Maximum Falling Path Sum
# Dynamic Programming - 2D DP

# Problem: Given an n x n matrix, find the minimum falling path sum. A falling path
# starts at any element in the first row and chooses the element from the next row
# that is either directly below or diagonally left/right below. Specifically, from
# position (row, col) you can move to (row+1, col-1), (row+1, col), or (row+1, col+1).

# Input: matrix = [[2, 1, 3],
#                  [6, 5, 4],
#                  [7, 8, 9]]
# Output: 13

# Explanation: Falling paths and their sums:
#   1 -> 5 -> 7 = 13 (minimum)
#   1 -> 4 -> 8 = 13 (also minimum)
#   2 -> 5 -> 7 = 14
#   Going through each starting column and picking the best path,
#   the minimum we can get is 13.

# Time Complexity: O(n * n) | Space Complexity: O(n)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n * n) | Space: O(n * n) for dp + O(n) recursion stack

def fallingPathMemo(i, j, matrix, n, dp):
    # Out of bounds for columns
    if j < 0 or j >= n:
        return float('inf')

    # Reached the first row
    if i == 0:
        return matrix[0][j]

    if dp[i][j] != -1:
        return dp[i][j]

    up = fallingPathMemo(i - 1, j, matrix, n, dp)
    leftDiag = fallingPathMemo(i - 1, j - 1, matrix, n, dp)
    rightDiag = fallingPathMemo(i - 1, j + 1, matrix, n, dp)

    dp[i][j] = matrix[i][j] + min(up, leftDiag, rightDiag)
    return dp[i][j]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n * n) | Space: O(n * n)

def fallingPathTabulation(matrix, n):
    dp = [[0] * n for _ in range(n)]

    # Base case: first row
    for j in range(n):
        dp[0][j] = matrix[0][j]

    for i in range(1, n):
        for j in range(n):
            up = dp[i - 1][j]

            leftDiag = dp[i - 1][j - 1] if j > 0 else float('inf')
            rightDiag = dp[i - 1][j + 1] if j < n - 1 else float('inf')

            dp[i][j] = matrix[i][j] + min(up, leftDiag, rightDiag)

    # Answer is the minimum in the last row
    return min(dp[n - 1])


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n * n) | Space: O(n)

def fallingPathSum(matrix, n):
    prev = list(matrix[0])

    for i in range(1, n):
        curr = [0] * n
        for j in range(n):
            up = prev[j]

            leftDiag = prev[j - 1] if j > 0 else float('inf')
            rightDiag = prev[j + 1] if j < n - 1 else float('inf')

            curr[j] = matrix[i][j] + min(up, leftDiag, rightDiag)
        prev = curr

    return min(prev)


matrix = [[2, 1, 3],
          [6, 5, 4],
          [7, 8, 9]]
n = len(matrix)

# Memoization
dp = [[-1] * n for _ in range(n)]
mini = float('inf')
for j in range(n):
    mini = min(mini, fallingPathMemo(n - 1, j, matrix, n, dp))
print(f"Memoization: {mini}")

# Tabulation
print(f"Tabulation: {fallingPathTabulation(matrix, n)}")

# Space Optimized
print(f"Space Optimized: {fallingPathSum(matrix, n)}")
