# 03. Maximum Sum of Non-Adjacent Elements (House Robber 1)
# Dynamic Programming - 1D DP

# Problem: Given an array of integers, find the maximum sum of a subsequence such that
# no two elements in the subsequence are adjacent in the original array.
# (Also known as House Robber / Maximum Sum without Adjacents)

# Input: nums = [2, 1, 4, 9]
# Output: 11

# Explanation: Pick elements at index 0 and 3 -> 2 + 9 = 11.
#   We cannot pick index 2 (value 4) and index 3 (value 9) together because
#   they are adjacent. 2 + 9 = 11 is the maximum possible sum.

# Time Complexity: O(n) | Space Complexity: O(1)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n) | Space: O(n) for dp array + O(n) recursion stack

def maxSumMemo(ind, nums, dp):
    if ind == 0:
        return nums[0]
    if ind < 0:
        return 0

    if dp[ind] != -1:
        return dp[ind]

    # Pick current element: add nums[ind] and skip adjacent (ind - 2)
    pick = nums[ind] + maxSumMemo(ind - 2, nums, dp)

    # Not pick current element: move to ind - 1
    notPick = maxSumMemo(ind - 1, nums, dp)

    dp[ind] = max(pick, notPick)
    return dp[ind]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n) | Space: O(n)

def maxSumTabulation(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        pick = nums[i] + dp[i - 2]
        notPick = dp[i - 1]
        dp[i] = max(pick, notPick)

    return dp[n - 1]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n) | Space: O(1)

def maxSum(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    prev2 = 0          # dp[i-2]
    prev1 = nums[0]    # dp[i-1]

    for i in range(1, n):
        pick = nums[i] + prev2
        notPick = prev1

        curr = max(pick, notPick)
        prev2 = prev1
        prev1 = curr

    return prev1


nums = [2, 1, 4, 9]

# Memoization
dp = [-1] * len(nums)
print(f"Memoization: {maxSumMemo(len(nums) - 1, nums, dp)}")

# Tabulation
print(f"Tabulation: {maxSumTabulation(nums)}")

# Space Optimized
print(f"Space Optimized: {maxSum(nums)}")
