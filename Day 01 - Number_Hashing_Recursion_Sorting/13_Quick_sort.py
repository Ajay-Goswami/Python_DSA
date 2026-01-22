# Quick Sort - Quick Sort is a divide-and-conquer sorting algorithm that sorts elements by selecting a pivot and partitioning the array around it.

# Time Complexity
# Best Case - O(nlogn) - Pivot divides array into equal halfs every time
# Average Case - O(nlogn) - Pivot divides array almost evenly
# Worst Case - O(n^2) - Pivot is always the smallest or largest element

# Space Complexity - O(logn)

# Ascending Order
import random
nums = [8, 9, 2, 5, 1, 7, 4, 6, 3]

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    # pivot = nums[0]
    pivot = random.choice(nums) # Using a random pivot reduces the chance of worst-case O(n²), which occurs when the pivot consistently becomes the smallest or largest element (e.g., sorted, reverse-sorted, or highly unbalanced input arrays).
    left = []
    right = []
    for i in range(1, len(nums)):
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(nums))