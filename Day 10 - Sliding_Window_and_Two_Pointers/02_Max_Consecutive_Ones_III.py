# Max Consecutive Ones III

# Leetcode : 1004

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6

def longestOnes(nums: list[int], k: int) -> int:  # Sliding Window Approach: O(N) time | O(1) space
    left = 0
    max_length = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))  # Output: 6