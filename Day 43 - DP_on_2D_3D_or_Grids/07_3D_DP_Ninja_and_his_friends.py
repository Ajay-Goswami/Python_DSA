# 07. 3D DP - Ninja and his Friends (Cherry Pickup 2)
# Dynamic Programming - 3D DP on Grid

# Problem: You have an r x c grid of chocolates. Two friends (Alice and Bob) start from
# the first row. Alice starts at (0, 0) and Bob starts at (0, c-1). They move to the
# next row simultaneously and can move to (row+1, col-1), (row+1, col), or (row+1, col+1).
# If both reach the same cell, only one of them picks up the chocolates. Find the maximum
# chocolates they can collect together reaching the last row.

# Input: grid = [[2, 3, 1, 2],
#                [3, 4, 2, 2],
#                [5, 6, 3, 5]]
# Output: 21

# Explanation: Alice goes (0,0)->(1,1)->(2,1) collecting 2+4+6 = 12
#   Bob goes (0,3)->(1,3)->(2,3) collecting 2+2+5 = 9
#   Total = 12 + 9 = 21. Since they never land on same cell no overlap issue.
#   This is the maximum possible collection.

# Time Complexity: O(r * c * c * 9) | Space Complexity: O(c * c)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(r * c * c * 9) | Space: O(r * c * c) for dp + O(r) recursion stack

def cherryMemo(i, j1, j2, r, c, grid, dp):
    # Out of bounds
    if j1 < 0 or j1 >= c or j2 < 0 or j2 >= c:
        return -1e8

    # Base case: reached last row
    if i == r - 1:
        if j1 == j2:
            return grid[i][j1]  # same cell, count only once
        else:
            return grid[i][j1] + grid[i][j2]

    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]

    maxi = -1e8
    # Both move simultaneously, 3 choices each = 9 combinations
    for dj1 in [-1, 0, 1]:
        for dj2 in [-1, 0, 1]:
            if j1 == j2:
                val = grid[i][j1] + cherryMemo(i + 1, j1 + dj1, j2 + dj2, r, c, grid, dp)
            else:
                val = grid[i][j1] + grid[i][j2] + cherryMemo(i + 1, j1 + dj1, j2 + dj2, r, c, grid, dp)
            maxi = max(maxi, val)

    dp[i][j1][j2] = maxi
    return dp[i][j1][j2]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(r * c * c * 9) | Space: O(r * c * c)

def cherryTabulation(r, c, grid):
    dp = [[[-1e8] * c for _ in range(c)] for _ in range(r)]

    # Base case: last row
    for j1 in range(c):
        for j2 in range(c):
            if j1 == j2:
                dp[r - 1][j1][j2] = grid[r - 1][j1]
            else:
                dp[r - 1][j1][j2] = grid[r - 1][j1] + grid[r - 1][j2]

    # Fill from second last row going upward
    for i in range(r - 2, -1, -1):
        for j1 in range(c):
            for j2 in range(c):
                maxi = -1e8
                for dj1 in [-1, 0, 1]:
                    for dj2 in [-1, 0, 1]:
                        nj1 = j1 + dj1
                        nj2 = j2 + dj2
                        if 0 <= nj1 < c and 0 <= nj2 < c:
                            if j1 == j2:
                                val = grid[i][j1] + dp[i + 1][nj1][nj2]
                            else:
                                val = grid[i][j1] + grid[i][j2] + dp[i + 1][nj1][nj2]
                            maxi = max(maxi, val)
                dp[i][j1][j2] = maxi

    return dp[0][0][c - 1]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(r * c * c * 9) | Space: O(c * c)

def cherryPickup(r, c, grid):
    # We only need current row and next row (front)
    front = [[-1e8] * c for _ in range(c)]

    # Base case: last row
    for j1 in range(c):
        for j2 in range(c):
            if j1 == j2:
                front[j1][j2] = grid[r - 1][j1]
            else:
                front[j1][j2] = grid[r - 1][j1] + grid[r - 1][j2]

    for i in range(r - 2, -1, -1):
        curr = [[-1e8] * c for _ in range(c)]
        for j1 in range(c):
            for j2 in range(c):
                maxi = -1e8
                for dj1 in [-1, 0, 1]:
                    for dj2 in [-1, 0, 1]:
                        nj1 = j1 + dj1
                        nj2 = j2 + dj2
                        if 0 <= nj1 < c and 0 <= nj2 < c:
                            if j1 == j2:
                                val = grid[i][j1] + front[nj1][nj2]
                            else:
                                val = grid[i][j1] + grid[i][j2] + front[nj1][nj2]
                            maxi = max(maxi, val)
                curr[j1][j2] = maxi
        front = curr

    return front[0][c - 1]


grid = [[2, 3, 1, 2],
        [3, 4, 2, 2],
        [5, 6, 3, 5]]
r = len(grid)
c = len(grid[0])

# Memoization
dp = [[[-1] * c for _ in range(c)] for _ in range(r)]
print(f"Memoization: {cherryMemo(0, 0, c - 1, r, c, grid, dp)}")

# Tabulation
print(f"Tabulation: {cherryTabulation(r, c, grid)}")

# Space Optimized
print(f"Space Optimized: {cherryPickup(r, c, grid)}")
