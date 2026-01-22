# Binary Search

# Time Complexity - O(logn)
# Space Complexity - O(1)

# Ascending Order
nums = [1, 7, 8, 4, 5, 6, 9, 2]
target = 6

# Iterative Binary Search
low = 0
high = len(nums) - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        print("Using Iterative Binary Search -> Index:", mid)
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(-1)


# Recursive Binary Search
def binary_search(nums, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums, target, mid + 1, high)
    else:
        return binary_search(nums, target, low, mid - 1)

print("Using Recursive Binary Search -> Index:", binary_search(nums, target, 0, len(nums) - 1))