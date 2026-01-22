# Lower Bound - Returns the index of the first element in the sorted array that is greater than or equal to the target value. (Smallest Index such that nums[index] >= target)
# Upper Bound - Returns the index of the first element in the sorted array that is greater than the target value. (Smallest Index such that nums[index] > target)

# Input : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and target = 5
# Output : 4th Index (Lower Bound) and 5th Index (Upper Bound)

# Time Complexity - O(logn)
# Space Complexity - O(1)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

def lower_bound(arr, target):
    low, high = 0, len(arr) 
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low  # first index where arr[i] >= target

def upper_bound(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low  # first index where arr[i] > target

print("Lower Bound Index:", lower_bound(nums, target))
print("Upper Bound Index:", upper_bound(nums, target))