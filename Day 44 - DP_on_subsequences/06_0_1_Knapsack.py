# 06. 0/1 Knapsack
# Dynamic Programming - DP on Subsequences

# Problem: Given N items, each with a weight and a value, and a knapsack
# with a maximum weight capacity W, find the maximum value that can be
# put in the knapsack. Each item can either be taken or not (0/1 choice).

# Input: wt = [3, 2, 5], val = [30, 40, 60], W = 6
# Output: 70

# Explanation: Take item 0 (wt=3, val=30) and item 1 (wt=2, val=40).
# Total weight = 3 + 2 = 5 <= 6, Total value = 30 + 40 = 70.
# Taking item 2 alone gives val=60 with wt=5, which is less than 70.

# Time Complexity: O(n * W) | Space Complexity: O(W)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n * W) | Space: O(n * W) for dp + O(n) recursion stack

def knapsackMemo(ind, W, wt, val, dp):
    if ind == 0:
        if wt[0] <= W:
            return val[0]
        return 0

    if dp[ind][W] != -1:
        return dp[ind][W]

    notTake = knapsackMemo(ind - 1, W, wt, val, dp)
    take = -1
    if wt[ind] <= W:
        take = val[ind] + knapsackMemo(ind - 1, W - wt[ind], wt, val, dp)

    dp[ind][W] = max(take, notTake)
    return dp[ind][W]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n * W) | Space: O(n * W)

def knapsackTabulation(n, W, wt, val):
    dp = [[0] * (W + 1) for _ in range(n)]

    # Base case: first item
    for w in range(wt[0], W + 1):
        dp[0][w] = val[0]

    for ind in range(1, n):
        for w in range(0, W + 1):
            notTake = dp[ind - 1][w]
            take = -1
            if wt[ind] <= w:
                take = val[ind] + dp[ind - 1][w - wt[ind]]
            dp[ind][w] = max(take, notTake)

    return dp[n - 1][W]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n * W) | Space: O(W)

def knapsackOptimized(n, W, wt, val):
    prev = [0] * (W + 1)

    # Base case: first item
    for w in range(wt[0], W + 1):
        prev[w] = val[0]

    for ind in range(1, n):
        curr = [0] * (W + 1)
        for w in range(0, W + 1):
            notTake = prev[w]
            take = -1
            if wt[ind] <= w:
                take = val[ind] + prev[w - wt[ind]]
            curr[w] = max(take, notTake)
        prev = curr

    return prev[W]


wt = [3, 2, 5]
val = [30, 40, 60]
W = 6
n = len(wt)

# Memoization
dp = [[-1] * (W + 1) for _ in range(n)]
print(f"Memoization: {knapsackMemo(n - 1, W, wt, val, dp)}")

# Tabulation
print(f"Tabulation: {knapsackTabulation(n, W, wt, val)}")

# Space Optimized
print(f"Space Optimized: {knapsackOptimized(n, W, wt, val)}")
