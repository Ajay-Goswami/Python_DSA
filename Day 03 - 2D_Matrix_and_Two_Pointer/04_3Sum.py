# 3 Sum - Leetcode 15
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

nums = [-1,0,1,2,-1,-4]
nums.sort()
res = []
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    l = i + 1
    r = len(nums) - 1
    while l < r:
        sum = nums[i] + nums[l] + nums[r]
        if sum > 0:
            r -= 1
        elif sum < 0:
            l += 1
        else:
            res.append([nums[i], nums[l], nums[r]])
            l += 1
            while l < r and nums[l] == nums[l-1]:
                l += 1
print(res)