# 01. Climbing Stairs
# Dynamic Programming - 1D DP

# Problem: You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways
# can you climb to the top?

# Input: n = 4
# Output: 5

# Explanation: There are 5 ways to climb to the top:
#   1. 1 + 1 + 1 + 1
#   2. 1 + 1 + 2
#   3. 1 + 2 + 1
#   4. 2 + 1 + 1
#   5. 2 + 2

# Time Complexity: O(n) | Space Complexity: O(1)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n) | Space: O(n) for dp array + O(n) recursion stack

def climbStairsMemo(n, dp):
    if n <= 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = climbStairsMemo(n - 1, dp) + climbStairsMemo(n - 2, dp)
    return dp[n]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n) | Space: O(n)

def climbStairsTabulation(n):
    if n <= 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n) | Space: O(1)

def climbStairs(n):
    if n <= 1:
        return 1

    prev2 = 1  # dp[0]
    prev1 = 1  # dp[1]

    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


n = 4

# Memoization
dp = [-1] * (n + 1)
print(f"Memoization: {climbStairsMemo(n, dp)}")

# Tabulation
print(f"Tabulation: {climbStairsTabulation(n)}")

# Space Optimized
print(f"Space Optimized: {climbStairs(n)}")
