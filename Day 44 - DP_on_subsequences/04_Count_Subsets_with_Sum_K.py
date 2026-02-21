# 04. Count Subsets with Sum K
# Dynamic Programming - DP on Subsequences

# Problem: Given an array of integers and a target sum K,
# count the number of subsets of the array that sum up to K.

# Input: arr = [1, 2, 2, 3], k = 3
# Output: 3

# Explanation: The subsets that sum to 3 are:
# {1, 2} (using first 2), {1, 2} (using second 2), {3}.
# Total count = 3.

# Time Complexity: O(n * k) | Space Complexity: O(k)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n * k) | Space: O(n * k) for dp + O(n) recursion stack

def countSubsetsMemo(ind, target, arr, dp):
    if target == 0:
        return 1
    if ind == 0:
        return 1 if arr[0] == target else 0
    if dp[ind][target] != -1:
        return dp[ind][target]

    notTake = countSubsetsMemo(ind - 1, target, arr, dp)
    take = 0
    if arr[ind] <= target:
        take = countSubsetsMemo(ind - 1, target - arr[ind], arr, dp)

    dp[ind][target] = take + notTake
    return dp[ind][target]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n * k) | Space: O(n * k)

def countSubsetsTabulation(n, k, arr):
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case: target 0 is always achievable (1 way - empty subset)
    for i in range(n):
        dp[i][0] = 1

    # Base case: first element
    if arr[0] <= k:
        dp[0][arr[0]] += 1

    for ind in range(1, n):
        for t in range(0, k + 1):
            notTake = dp[ind - 1][t]
            take = 0
            if arr[ind] <= t:
                take = dp[ind - 1][t - arr[ind]]
            dp[ind][t] = take + notTake

    return dp[n - 1][k]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n * k) | Space: O(k)

def countSubsetsOptimized(n, k, arr):
    prev = [0] * (k + 1)
    prev[0] = 1

    if arr[0] <= k:
        prev[arr[0]] += 1

    for ind in range(1, n):
        curr = [0] * (k + 1)
        curr[0] = 1
        for t in range(0, k + 1):
            notTake = prev[t]
            take = 0
            if arr[ind] <= t:
                take = prev[t - arr[ind]]
            curr[t] = take + notTake
        prev = curr

    return prev[k]


arr = [1, 2, 2, 3]
k = 3
n = len(arr)

# Memoization
dp = [[-1] * (k + 1) for _ in range(n)]
print(f"Memoization: {countSubsetsMemo(n - 1, k, arr, dp)}")

# Tabulation
print(f"Tabulation: {countSubsetsTabulation(n, k, arr)}")

# Space Optimized
print(f"Space Optimized: {countSubsetsOptimized(n, k, arr)}")
