# 02. Partition Equal Subset Sum
# Dynamic Programming - DP on Subsequences

# Problem: Given an array of positive integers, determine if the array can be
# partitioned into two subsets such that the sum of elements in both subsets
# is equal.

# Input: arr = [2, 3, 3, 3, 4, 5]
# Output: True

# Explanation: Total sum = 20, so each subset must sum to 10.
# One valid partition: {2, 3, 5} and {3, 3, 4}, both sum to 10.

# Time Complexity: O(n * totalSum/2) | Space Complexity: O(totalSum/2)


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


def partitionMemo(arr):
    totalSum = sum(arr)
    if totalSum % 2 != 0:
        return False
    target = totalSum // 2
    n = len(arr)
    dp = [[-1] * (target + 1) for _ in range(n)]
    return subsetSumMemo(n - 1, target, arr, dp)


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n * target) | Space: O(n * target)

def partitionTabulation(arr):
    totalSum = sum(arr)
    if totalSum % 2 != 0:
        return False
    target = totalSum // 2
    n = len(arr)

    dp = [[False] * (target + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = True

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

def partitionOptimized(arr):
    totalSum = sum(arr)
    if totalSum % 2 != 0:
        return False
    target = totalSum // 2
    n = len(arr)

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


arr = [2, 3, 3, 3, 4, 5]

# Memoization
print(f"Memoization: {partitionMemo(arr)}")

# Tabulation
print(f"Tabulation: {partitionTabulation(arr)}")

# Space Optimized
print(f"Space Optimized: {partitionOptimized(arr)}")
