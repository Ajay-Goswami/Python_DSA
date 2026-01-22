# Insertion Sort - A sorting algorithm that builds the final sorted array one item at a time.

# Time Complexity in Worst Case and Average Case - O(n^2), Best Case - O(n)
# Space Complexity - O(1)

# Bubble → compare & swap → slow
# Selection → minimum find → fixed cost
# Insertion → insert in place → best for nearly sorted

# Ascending Order
nums = [8, 9, 2, 5, 1, 7, 4, 6, 3]

for i in range(1, len(nums)):
    key = nums[i]        # element to insert
    j = i - 1
    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]  # shift right
        j -= 1
    nums[j + 1] = key   # insert once

print(nums)

# Descending Order
for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and nums[j] < key:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key

print(nums)