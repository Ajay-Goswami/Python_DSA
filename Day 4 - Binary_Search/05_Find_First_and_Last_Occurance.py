# Find First and Last Occurance

# Leetcode - 34
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

nums = [5, 7, 7, 8, 8, 10]
target = 8

# Brute Force -> Time Complexity -> O(n), Space Complexity -> O(1)
def first_last_occurance(nums, target):
    first = -1
    last = -1
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
        if nums[i] > target:
            break
    return [first, last]
print("First and Last Occurance Using Brute Force ->", first_last_occurance(nums, target))

# Optimal Solution -> Time Complexity -> O(logn), Space Complexity -> O(1)
def first_last_occurance(nums, target):
    def lower_bound(arr, target):
        low, high = 0, len(arr) 
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low  
    def upper_bound(arr, target):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return low 
    return [lower_bound(nums, target), upper_bound(nums, target) - 1]

print("First and Last Occurance Using Binary Search ->", first_last_occurance(nums, target))