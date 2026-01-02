# Find Missing Number from an array - 
# Given an array of n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Input: nums = [3,0,1,2,5]
# Output: 4

nums = [3,0,1,2,5]

#Brute Force -> O(n^2)
for i in range(len(nums)): # O(n)
    if i not in nums: # O(n)
        print(i)
        break

#Little Optimized -> O(nlogn)
nums.sort() # O(nlogn)
for i in range(len(nums)): # O(n)
    if i != nums[i]:
        print(i)
        break

#Optimal Solution -> O(n)
print(len(nums)*(len(nums)+1)//2 - sum(nums)) # n*(n+1)/2 - sum -> O(n)