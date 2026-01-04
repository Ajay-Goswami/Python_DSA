# Find the minimum element in rotated sorted array

# Input: nums = [8,9,0,3,5,6,7]
# Output: 0

nums = [7,8,9,1,2,3,4]

n = len(nums)
low = 0
high = n - 1
minimum = float('inf')
while low <= high:
    mid = (low + high) //2
    if nums[mid]<=nums[high]:
        minimum = min(minimum, nums[mid])
        high = mid - 1
    else:
        minimum = min(minimum, nums[low])
        low = mid + 1

print(minimum)

