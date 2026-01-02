# Longest Consecutive Sequence - 
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Input : nums = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]
# Output : 4 ->(99, 100, 101, 102)

nums = [1, 99, 101, 98, 2, 5, 3, 99, 100]
n = len(nums)

# Brute Force -> O(n^2)
max_count = 0
for i in range(0,n): # O(n)
    num = nums[i]
    count = 1
    while num+1 in nums: # O(n)
        count += 1
        num += 1
    max_count = max(max_count, count)
print(max_count)

# Better Solution -> O(nlogn + n)
nums.sort() # O(nlogn)
count = 0
last_smallest = float('-inf')
longest = 0
for i in range(0, n):
    num = nums[i]
    if num - 1 == last_smallest:
        count += 1
        longest = max(longest, count)
    elif num == last_smallest:
        continue
    else:
        count = 1
        longest = max(longest, count)
    last_smallest = num

print(longest)


# Optimized Solution ->  Time Complexity-> O(n),  Space Complexity-> O(n)
nums = [1, 99, 101, 98, 2, 5, 3, 99, 100]
n = len(nums)
nums = set(nums) # O(n)
longest = 0
for num in nums: # O(n)
    if num-1 not in nums:
        count = 1
        while num+1 in nums: # O(1)
            count += 1
            num += 1
        longest = max(longest, count)
print(longest)