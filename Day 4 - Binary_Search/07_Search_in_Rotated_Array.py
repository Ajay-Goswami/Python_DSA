# Search in Rotated Array 

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4 th Index

# Without Duplicates
nums = [4,5,6,7,9,1,2]
target = 1

def search_without_duplicates(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]: # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else: # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1



# With Duplicates
d_nums = [4,5,5,6,7,0,1,2,2,2]
d_target = 5

def search_with_duplicates(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target: 
            return mid
        if nums[left] == nums[mid] == nums[right]: # All elements are equal
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]: # Left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else: # Right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


print("Without Duplicates:", search_without_duplicates(nums, target), "th Index")
print("With Duplicates:", search_with_duplicates(d_nums, d_target), "th Index")