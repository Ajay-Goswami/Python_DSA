# Count the occurance of a number 

# Input : nums = [1,2,3,3,3,3,3,5,6,8,9,9,10] Target = 3
# Output : 5

nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
target = 3

# Brute Force -> Time Complexity -> O(n), Space Complexity -> O(1)
count = 0
for i in range(len(nums)):
    if nums[i] == target:
        count += 1

print("Count Using Brute Force ->", count)


# Optimal Solution -> Time Complexity -> O(logn)
import bisect
def count_occurrences_optimal(nums, target):
    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target)
    return right - left

count_optimal = count_occurrences_optimal(nums, target)
print("Count Using Optimal Solution ->", count_optimal)
