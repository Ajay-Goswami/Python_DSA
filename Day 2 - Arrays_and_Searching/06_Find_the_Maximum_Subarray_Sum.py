# Find the maximum subarray sum - 
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

nums = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = nums[0]
curr_sum = nums[0]
for i in range(1, len(nums)):
    curr_sum = max(curr_sum + nums[i], nums[i])
    max_sum = max(max_sum, curr_sum)

print(max_sum)
