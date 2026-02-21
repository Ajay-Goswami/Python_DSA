# 05. Count Partitions with Given Difference
# Dynamic Programming - DP on Subsequences

# Problem: Given an array of integers and a difference D,
# count the number of ways to partition the array into two subsets
# S1 and S2 such that S1 - S2 = D (where S1 >= S2).

# Input: arr = [5, 2, 6, 4], d = 3
# Output: 1

# Explanation: Total sum = 17.
# S1 - S2 = D and S1 + S2 = totalSum
# => S1 = (totalSum + D) / 2 = (17 + 3) / 2 = 10
# We need to count subsets with sum = 10.
# Only {4, 6} sums to 10. So count = 1.

# Time Complexity: O(n * target) | Space Complexity: O(target)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n * target) | Space: O(n * target) for dp + O(n) recursion stack

def countSubsetsMemo(ind, target, arr, dp):
    if ind == 0:
        if target == 0 and arr[0] == 0:
            return 2  # take or not take the 0
        if target == 0 or arr[0] == target:
            return 1
        return 0

    if dp[ind][target] != -1:
        return dp[ind][target]

    notTake = countSubsetsMemo(ind - 1, target, arr, dp)
    take = 0
    if arr[ind] <= target:
        take = countSubsetsMemo(ind - 1, target - arr[ind], arr, dp)

    dp[ind][target] = take + notTake
    return dp[ind][target]


def countPartitionsMemo(arr, d):
    totalSum = sum(arr)
    if (totalSum + d) % 2 != 0:
        return 0
    target = (totalSum + d) // 2
    if target < 0:
        return 0
    n = len(arr)
    dp = [[-1] * (target + 1) for _ in range(n)]
    return countSubsetsMemo(n - 1, target, arr, dp)


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n * target) | Space: O(n * target)

def countPartitionsTabulation(arr, d):
    n = len(arr)
    totalSum = sum(arr)
    if (totalSum + d) % 2 != 0:
        return 0
    target = (totalSum + d) // 2
    if target < 0:
        return 0

    dp = [[0] * (target + 1) for _ in range(n)]

    # Base cases
    if arr[0] == 0:
        dp[0][0] = 2  # take or not take the 0
    else:
        dp[0][0] = 1

    if arr[0] != 0 and arr[0] <= target:
        dp[0][arr[0]] = 1

    for ind in range(1, n):
        for t in range(0, target + 1):
            notTake = dp[ind - 1][t]
            take = 0
            if arr[ind] <= t:
                take = dp[ind - 1][t - arr[ind]]
            dp[ind][t] = take + notTake

    return dp[n - 1][target]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n * target) | Space: O(target)

def countPartitionsOptimized(arr, d):
    n = len(arr)
    totalSum = sum(arr)
    if (totalSum + d) % 2 != 0:
        return 0
    target = (totalSum + d) // 2
    if target < 0:
        return 0

    prev = [0] * (target + 1)

    if arr[0] == 0:
        prev[0] = 2
    else:
        prev[0] = 1

    if arr[0] != 0 and arr[0] <= target:
        prev[arr[0]] = 1

    for ind in range(1, n):
        curr = [0] * (target + 1)
        for t in range(0, target + 1):
            notTake = prev[t]
            take = 0
            if arr[ind] <= t:
                take = prev[t - arr[ind]]
            curr[t] = take + notTake
        prev = curr

    return prev[target]


arr = [5, 2, 6, 4]
d = 3

# Memoization
print(f"Memoization: {countPartitionsMemo(arr, d)}")

# Tabulation
print(f"Tabulation: {countPartitionsTabulation(arr, d)}")

# Space Optimized
print(f"Space Optimized: {countPartitionsOptimized(arr, d)}")
