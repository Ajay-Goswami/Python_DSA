# Kth Largest Element in an Array
# Leetcode - 215
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

nums = [3, 2, 1, 5, 6, 4]
k = 2

# Brute Force -> Time Complexity -> O(n log n), Space Complexity -> O(1)
def kth_largest_bruteforce(nums, k):
    nums.sort()
    return nums[len(nums) - k]

print("Kth Largest Element Using Brute Force ->", kth_largest_bruteforce(nums, k))


import heapq

# Optimal Solution Using Priority Queue (Min Heap)
# Time Complexity -> O(n log k), Space Complexity -> O(k)
def kth_largest_priority_queue(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

print("Kth Largest Element Using Priority Queue ->", kth_largest_priority_queue(nums, k))