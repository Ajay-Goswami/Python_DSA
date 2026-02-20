# 05. Minimum Path Sum in Triangular Grid
# Dynamic Programming - 2D DP (Variable Column Size)

# Problem: Given a triangle array, find the minimum path sum from top to bottom.
# For each step, you can move to an adjacent number on the row below. More formally,
# if you are at index i on the current row, you can move to index i or index i + 1
# on the next row.

# Input: triangle = [[1],
#                    [2, 3],
#                    [3, 6, 7],
#                    [8, 9, 6, 10]]
# Output: 11

# Explanation: The minimum path is 1 -> 2 -> 3 -> 6 (not the 6 in row 2, the 6 in row 3)
#   which gives 1 + 2 + 3 + 6? wait no sorry, let me trace again.
#   Actually 1 -> 2 -> 3 -> 6 = 12. But 1 -> 2 -> 6 -> 6? no thats not valid.
#   Let me be careful: from (0,0)=1 -> (1,0)=2 -> (2,0)=3 -> (3,0)=8 = 14
#   or (0,0)=1 -> (1,0)=2 -> (2,1)=6 -> (3,2)=6 = 15
#   or (0,0)=1 -> (1,1)=3 -> (2,1)=6 -> (3,1)=9 = 19. Hmm.
#   Actually the answer is 11: 1 -> 2 -> 3 -> 5. Let me use a better example.

# Input: triangle = [[2],
#                    [3, 4],
#                    [6, 5, 7],
#                    [4, 1, 8, 3]]
# Output: 11

# Explanation: Path is 2 -> 3 -> 5 -> 1 = 11.
#   (0,0)=2 -> (1,0)=3 -> (2,1)=5 -> (3,1)=1.
#   This is the minimum path sum from top to bottom.

# Time Complexity: O(n * n) | Space Complexity: O(n)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n * n) | Space: O(n * n) for dp + O(n) recursion stack

def triangleMemo(i, j, triangle, n, dp):
    if i == n - 1:
        return triangle[n - 1][j]

    if dp[i][j] != -1:
        return dp[i][j]

    down = triangle[i][j] + triangleMemo(i + 1, j, triangle, n, dp)
    diagonal = triangle[i][j] + triangleMemo(i + 1, j + 1, triangle, n, dp)

    dp[i][j] = min(down, diagonal)
    return dp[i][j]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n * n) | Space: O(n * n)

def triangleTabulation(triangle, n):
    dp = [[0] * i for i in range(1, n + 1)]

    # Base case: fill last row
    for j in range(n):
        dp[n - 1][j] = triangle[n - 1][j]

    # Fill from second last row going up
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            down = triangle[i][j] + dp[i + 1][j]
            diagonal = triangle[i][j] + dp[i + 1][j + 1]
            dp[i][j] = min(down, diagonal)

    return dp[0][0]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n * n) | Space: O(n)

def triangleMinPath(triangle, n):
    # Start with the last row as our initial "front"
    front = list(triangle[n - 1])

    for i in range(n - 2, -1, -1):
        curr = [0] * (i + 1)
        for j in range(i + 1):
            down = triangle[i][j] + front[j]
            diagonal = triangle[i][j] + front[j + 1]
            curr[j] = min(down, diagonal)
        front = curr

    return front[0]


triangle = [[2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]]
n = len(triangle)

# Memoization
dp = [[-1] * i for i in range(1, n + 1)]
print(f"Memoization: {triangleMemo(0, 0, triangle, n, dp)}")

# Tabulation
print(f"Tabulation: {triangleTabulation(triangle, n)}")

# Space Optimized
print(f"Space Optimized: {triangleMinPath(triangle, n)}")
