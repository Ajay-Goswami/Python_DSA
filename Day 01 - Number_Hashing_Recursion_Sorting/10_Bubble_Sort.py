# Bubble Sort - A sorting algorithm that compares adjacent elements and swaps them if they are in the wrong order.

# Time Complexity in Worst Case and Average Case - O(n^2), Best Case - O(n)
# Space Complexity - O(1)

# Bubble → compare & swap → slow
# Selection → minimum find → fixed cost
# Insertion → insert in place → best for nearly sorted

# In Ascending Order
nums = [1, 7, 8, 4, 5, 3, 9, 4, 2]
for i in range(len(nums)-2, -1, -1):
    is_swap = False
    for j in range(0, i+1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            is_swap = True
    if not is_swap:
        break

print(nums)

# In Descending Order
nums = [1, 7, 8, 4, 5, 3, 9, 4, 2]
for i in range(len(nums)-2, -1, -1):
    flag = True
    for j in range(0, i+1):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            flag = False
    if flag:
        break

print(nums)
