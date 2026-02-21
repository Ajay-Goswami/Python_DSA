# 03. Partition Set Into 2 Subsets With Minimum Absolute Sum Difference
# Dynamic Programming - DP on Subsequences

# Problem: Given an array of integers, partition it into two subsets S1 and S2
# such that the absolute difference of their sums |S1 - S2| is minimized.
# Return the minimum absolute difference.

# Input: arr = [1, 2, 3, 4]
# Output: 0

# Explanation: Total sum = 10. We can split into {1, 4} and {2, 3}
# with sums 5 and 5. |5 - 5| = 0.
# Alternatively {1, 2, 3} = 6 and {4} = 4 gives |6 - 4| = 2, which is worse.

# Time Complexity: O(n * totalSum) | Space Complexity: O(totalSum)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n * totalSum) | Space: O(n * totalSum) for dp + O(n) recursion stack

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


def minSubsetSumDiffMemo(arr):
    n = len(arr)
    totalSum = sum(arr)
    dp = [[-1] * (totalSum + 1) for _ in range(n)]

    # Fill dp for all possible targets from 0 to totalSum
    for t in range(totalSum + 1):
        subsetSumMemo(n - 1, t, arr, dp)

    mini = float('inf')
    for s1 in range(totalSum + 1):
        if dp[n - 1][s1] == True:
            s2 = totalSum - s1
            mini = min(mini, abs(s1 - s2))

    return mini


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n * totalSum) | Space: O(n * totalSum)

def minSubsetSumDiffTabulation(arr):
    n = len(arr)
    totalSum = sum(arr)

    dp = [[False] * (totalSum + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = True

    if arr[0] <= totalSum:
        dp[0][arr[0]] = True

    for ind in range(1, n):
        for t in range(1, totalSum + 1):
            notTake = dp[ind - 1][t]
            take = False
            if arr[ind] <= t:
                take = dp[ind - 1][t - arr[ind]]
            dp[ind][t] = take or notTake

    mini = float('inf')
    for s1 in range(totalSum + 1):
        if dp[n - 1][s1]:
            s2 = totalSum - s1
            mini = min(mini, abs(s1 - s2))

    return mini


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n * totalSum) | Space: O(totalSum)

def minSubsetSumDiffOptimized(arr):
    n = len(arr)
    totalSum = sum(arr)

    prev = [False] * (totalSum + 1)
    prev[0] = True

    if arr[0] <= totalSum:
        prev[arr[0]] = True

    for ind in range(1, n):
        curr = [False] * (totalSum + 1)
        curr[0] = True
        for t in range(1, totalSum + 1):
            notTake = prev[t]
            take = False
            if arr[ind] <= t:
                take = prev[t - arr[ind]]
            curr[t] = take or notTake
        prev = curr

    mini = float('inf')
    for s1 in range(totalSum // 2 + 1):
        if prev[s1]:
            s2 = totalSum - s1
            mini = min(mini, abs(s1 - s2))

    return mini


arr = [1, 2, 3, 4]

# Memoization
print(f"Memoization: {minSubsetSumDiffMemo(arr)}")

# Tabulation
print(f"Tabulation: {minSubsetSumDiffTabulation(arr)}")

# Space Optimized
print(f"Space Optimized: {minSubsetSumDiffOptimized(arr)}")
