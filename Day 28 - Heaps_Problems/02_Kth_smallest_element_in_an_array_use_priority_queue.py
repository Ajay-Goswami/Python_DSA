# Kth Smallest Element in an Array
# Given an integer array nums and an integer k, return the kth smallest element in the array.
# The kth smallest element is the element that would appear at index k-1 after sorting.

# Input: nums = [7,10,4,3,20,15], k = 3
# Output: 7

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 2

nums = [7, 10, 4, 3, 20, 15]
k = 3

# Brute Force -> Time Complexity -> O(n log n), Space Complexity -> O(1)
def kth_smallest_bruteforce(nums, k):
    nums.sort()
    return nums[k - 1]

print("Kth Smallest Element Using Brute Force ->", kth_smallest_bruteforce(nums, k))


import heapq

# Optimal Solution Using Priority Queue (Max Heap)
# Time Complexity -> O(n log k), Space Complexity -> O(k)
def kth_smallest_priority_queue(nums, k):
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return -max_heap[0]

print("Kth Smallest Element Using Priority Queue ->", kth_smallest_priority_queue(nums, k))