# Two Sum Problem - 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [5, 9, 1, 2, 4, 15, 6, 3], target = 13
# Output: [1, 4] -> Because nums[1] + nums[4] == 13

nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 13

# Brute Force - O(n^2)
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
            break

# Optimal Solution - O(n)
nums_dict = {}
for i in range(len(nums)):
    if target - nums[i] in nums_dict:
        print(nums_dict[target - nums[i]], i)
        break
    nums_dict[nums[i]] = i
