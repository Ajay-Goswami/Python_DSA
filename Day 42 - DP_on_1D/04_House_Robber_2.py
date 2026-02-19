# 04. House Robber 2
# Dynamic Programming - 1D DP

# Problem: You are a robber planning to rob houses along a street. Each house has a certain
# amount of money stashed. All houses are arranged in a CIRCLE, meaning the first house is
# the neighbor of the last house. You cannot rob two adjacent houses. Find the maximum
# amount of money you can rob without alerting the police.

# Input: nums = [2, 3, 2]
# Output: 3

# Explanation: Since houses are in a circle, house 0 and house 2 are adjacent.
#   You cannot rob both house 0 (money=2) and house 2 (money=2).
#   Best option: rob house 1 (money=3). Maximum = 3.

# Input: nums = [1, 2, 3, 1]
# Output: 4

# Explanation: Rob house 0 (money=1) and house 2 (money=3) = 1 + 3 = 4.
#   House 0 and house 3 are adjacent (circular), so we can't pick both.
#   House 1 and house 3 are not adjacent, but 2 + 1 = 3 < 4.

# Approach: Since first and last houses are adjacent (circular), we solve two subproblems:
#   1. Consider houses from index 0 to n-2 (exclude last house)
#   2. Consider houses from index 1 to n-1 (exclude first house)
#   Answer = max of both subproblems.
#   Each subproblem is the standard House Robber (non-adjacent max sum).

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

    pick = nums[ind] + maxSumMemo(ind - 2, nums, dp)
    notPick = maxSumMemo(ind - 1, nums, dp)

    dp[ind] = max(pick, notPick)
    return dp[ind]


def houseRobber2Memo(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    # Exclude last house (index 0 to n-2)
    dp1 = [-1] * (n - 1)
    excludeLast = maxSumMemo(n - 2, nums[:-1], dp1)

    # Exclude first house (index 1 to n-1)
    dp2 = [-1] * (n - 1)
    excludeFirst = maxSumMemo(n - 2, nums[1:], dp2)

    return max(excludeLast, excludeFirst)


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n) | Space: O(n)

def maxSumTabulation(nums):
    n = len(nums)
    if n == 0:
        return 0
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


def houseRobber2Tabulation(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    excludeLast = maxSumTabulation(nums[:-1])
    excludeFirst = maxSumTabulation(nums[1:])

    return max(excludeLast, excludeFirst)


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n) | Space: O(1)

def maxSumOptimized(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    prev2 = 0
    prev1 = nums[0]

    for i in range(1, n):
        pick = nums[i] + prev2
        notPick = prev1

        curr = max(pick, notPick)
        prev2 = prev1
        prev1 = curr

    return prev1


def houseRobber2(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    excludeLast = maxSumOptimized(nums[:-1])
    excludeFirst = maxSumOptimized(nums[1:])

    return max(excludeLast, excludeFirst)


nums1 = [2, 3, 2]
nums2 = [1, 2, 3, 1]

# Memoization
print(f"Memoization: {nums1} -> {houseRobber2Memo(nums1)}")
print(f"Memoization: {nums2} -> {houseRobber2Memo(nums2)}")

# Tabulation
print(f"Tabulation: {nums1} -> {houseRobber2Tabulation(nums1)}")
print(f"Tabulation: {nums2} -> {houseRobber2Tabulation(nums2)}")

# Space Optimized
print(f"Space Optimized: {nums1} -> {houseRobber2(nums1)}")
print(f"Space Optimized: {nums2} -> {houseRobber2(nums2)}")
