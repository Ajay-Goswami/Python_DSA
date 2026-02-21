# 01. Subset Sum Equal to Target
# Dynamic Programming - DP on Subsequences

# Problem: Given an array of non-negative integers and a target sum,
# determine if there exists a subset of the array whose elements sum up
# to the given target.

# Input: arr = [1, 2, 3, 4], target = 4
# Output: True

# Explanation: Subsets that sum to 4: {4}, {1, 3}.
# Since at least one subset exists, the answer is True.

# Time Complexity: O(n * target) | Space Complexity: O(target)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n * target) | Space: O(n * target) for dp + O(n) recursion stack

def subsetSumMemo(ind, target, arr, dp):
    if target == 0:
        return True
    if ind == 0:
        return arr[0] == target
    if dp[ind][target] != -1:
        return dp[ind][target]

    notTake = subsetSumMemo(ind - 1, target, arr, dp)
    take = False
    if arr[ind] <= target:
        take = subsetSumMemo(ind - 1, target - arr[ind], arr, dp)

    dp[ind][target] = take or notTake
    return dp[ind][target]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n * target) | Space: O(n * target)

def subsetSumTabulation(n, target, arr):
    dp = [[False] * (target + 1) for _ in range(n)]

    # Base case: target 0 is always achievable (empty subset)
    for i in range(n):
        dp[i][0] = True

    # Base case: first element can achieve target == arr[0]
    if arr[0] <= target:
        dp[0][arr[0]] = True

    for ind in range(1, n):
        for t in range(1, target + 1):
            notTake = dp[ind - 1][t]
            take = False
            if arr[ind] <= t:
                take = dp[ind - 1][t - arr[ind]]
            dp[ind][t] = take or notTake

    return dp[n - 1][target]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n * target) | Space: O(target)

def subsetSumOptimized(n, target, arr):
    prev = [False] * (target + 1)
    prev[0] = True

    if arr[0] <= target:
        prev[arr[0]] = True

    for ind in range(1, n):
        curr = [False] * (target + 1)
        curr[0] = True
        for t in range(1, target + 1):
            notTake = prev[t]
            take = False
            if arr[ind] <= t:
                take = prev[t - arr[ind]]
            curr[t] = take or notTake
        prev = curr

    return prev[target]


arr = [1, 2, 3, 4]
target = 4
n = len(arr)

# Memoization
dp = [[-1] * (target + 1) for _ in range(n)]
print(f"Memoization: {subsetSumMemo(n - 1, target, arr, dp)}")

# Tabulation
print(f"Tabulation: {subsetSumTabulation(n, target, arr)}")

# Space Optimized
print(f"Space Optimized: {subsetSumOptimized(n, target, arr)}")
