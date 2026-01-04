# Floor and Ceil in Sorted Array

# Floor - Smallest number in an array >= target
# Ceil - Largest number in an array <= target


# Input : [3,4,4,4,8,9,9,10,12,12,14,15]
# Target = 8 -> Floor = 8, Ceil = 8
# Target = 11 -> Floor = 10, Ceil = 12
# Target = 2 -> Floor = -1, Ceil = 3
# Target = 20 -> Floor = 15, Ceil = -1

nums = [3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15]
target = 20

def floor_ceil(nums, target):
    low = 0
    high = len(nums) - 1
    floor = -1
    ceil = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return [nums[mid], nums[mid]]
        elif nums[mid] < target:
            low = mid + 1
            floor = nums[mid]
        else:
            high = mid - 1
            ceil = nums[mid]
    return [floor, ceil]

print(floor_ceil(nums, target))