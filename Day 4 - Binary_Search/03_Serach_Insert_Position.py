# Search Insert Position - Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

# Leetcode - 35

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,4,5,8,9,12,15], target = 7
# Output: 4

# Time Complexity - O(logn)
# Space Complexity - O(1)

nums = [1, 3, 4, 5, 8, 9, 12, 15]
target = 7
def searchInsert(nums, target):
    lb = 0
    low = 0
    high = len(nums) - 1
    while low<=high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            high = mid - 1
            lb = mid
        else:
            low = mid + 1
    return lb
print("Insert Position -> Index:", searchInsert(nums, target))
    