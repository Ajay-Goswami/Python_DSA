# 4 Sum - Leetcode 18
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# nums = [1,0,-1,0,-2,2]
# target = 0
nums = [2,2,2,2]
target = 8

def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            l = j + 1
            r = n - 1
            while l < r:
                sum = nums[i] + nums[j] + nums[l] + nums[r]
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
    return res

print(four_sum(nums, target))