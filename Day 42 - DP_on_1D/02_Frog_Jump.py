# 02. Frog Jump
# Dynamic Programming - 1D DP

# Problem: A frog is at the first step and wants to reach the Nth step. The frog can jump
# either 1 step or 2 steps at a time. The cost of a jump from step i to step j is
# abs(height[i] - height[j]). Find the minimum total cost to reach the Nth step.

# Input: n = 4, height = [10, 20, 30, 10]
# Output: 20

# Explanation: The frog can jump from step 0 -> 1 -> 3
#   Cost = |10 - 20| + |20 - 10| = 10 + 10 = 20
#   This is the minimum cost path. Going 0 -> 1 -> 2 -> 3 would cost
#   |10-20| + |20-30| + |30-10| = 10 + 10 + 20 = 40.

# Time Complexity: O(n) | Space Complexity: O(1)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n) | Space: O(n) for dp array + O(n) recursion stack

def frogJumpMemo(ind, height, dp):
    if ind == 0:
        return 0

    if dp[ind] != -1:
        return dp[ind]

    oneStep = frogJumpMemo(ind - 1, height, dp) + abs(height[ind] - height[ind - 1])

    twoStep = float('inf')
    if ind > 1:
        twoStep = frogJumpMemo(ind - 2, height, dp) + abs(height[ind] - height[ind - 2])

    dp[ind] = min(oneStep, twoStep)
    return dp[ind]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n) | Space: O(n)

def frogJumpTabulation(n, height):
    dp = [0] * n
    dp[0] = 0

    for i in range(1, n):
        oneStep = dp[i - 1] + abs(height[i] - height[i - 1])

        twoStep = float('inf')
        if i > 1:
            twoStep = dp[i - 2] + abs(height[i] - height[i - 2])

        dp[i] = min(oneStep, twoStep)

    return dp[n - 1]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n) | Space: O(1)

def frogJump(n, height):
    prev2 = 0  # dp[0]
    prev1 = 0  # dp[0] initially, will be updated

    for i in range(1, n):
        oneStep = prev1 + abs(height[i] - height[i - 1])

        twoStep = float('inf')
        if i > 1:
            twoStep = prev2 + abs(height[i] - height[i - 2])

        curr = min(oneStep, twoStep)
        prev2 = prev1
        prev1 = curr

    return prev1


n = 4
height = [10, 20, 30, 10]

# Memoization
dp = [-1] * n
print(f"Memoization: {frogJumpMemo(n - 1, height, dp)}")

# Tabulation
print(f"Tabulation: {frogJumpTabulation(n, height)}")

# Space Optimized
print(f"Space Optimized: {frogJump(n, height)}")
