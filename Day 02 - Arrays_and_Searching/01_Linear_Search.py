# Linear Search - A search algorithm that sequentially checks each element of a list until a match is found or the entire list has been searched.

# Time Complexity - O(n)
# Space Complexity - O(1)

nums = [1, 7, 8, 4, 5, 6, 9, 2]
target = 13

for i in range(len(nums)):
    if nums[i] == target:
        print(i)
        break
else:
    print(-1)

