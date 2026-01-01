# Selection Sort : A sorting algorithm that selects the smallest element from an unsorted list in each iteration and places it at the beginning of the sorted list.

# Time Complexity in Worst Case, Best Case, Average Case - O(n^2)
# Space Complexity - O(1)

# Bubble → compare & swap → slow
# Selection → minimum find → fixed cost
# Insertion → insert in place → best for nearly sorted

# In Ascending Order-
nums = [1, 7, 8, 4, 5, 6, 9, 2]
for i in range(len(nums)):
    min_idx = i
    for j in range(i+1, len(nums)):
        if nums[j]<nums[min_idx]:
            min_idx = j
    nums[i] , nums[min_idx] = nums[min_idx], nums[i]

print(nums)

# In Descending Order -
nums = [1, 7, 8, 4, 5, 6, 9, 2]
for i in range(len(nums)):
    max_idx =i
    for j in range(i+1, len(nums)):
        if nums[j]>nums[max_idx]:
            max_idx = j
    nums[i] , nums[max_idx] = nums[max_idx], nums[i]

print(nums)