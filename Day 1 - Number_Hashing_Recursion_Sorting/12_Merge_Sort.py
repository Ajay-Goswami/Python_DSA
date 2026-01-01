# Merge Sort (Divide and Conquer/Merge) - A sorting algorithm that divides the input into two halves, calls itself for the two halves and then merges the two sorted halves.

# Time Complexity in Worst Case, Best Case, Average Case - O(nlogn)
# Space Complexity - O(n)

nums = [1, 7, 8, 4, 5, 6, 9, 2]

# In Ascending Order
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

print(merge_sort(nums))