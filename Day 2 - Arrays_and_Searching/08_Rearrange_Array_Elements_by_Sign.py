# Rearrange Array Elements by Sign -
# Given an array nums of integers, we have to rearrange the elements in alternative order positive then negative then positive like that. We have given equal number of positive and negative numbers.

# Input - nums = [5, 10, -3, -1, -10, 6]
# Output - [5, -3, 10, -1, 6, -10]


# Brute force - Time Complexity-> O(n + n//2) -> Space Complexity-> O(n)
nums = [5, 10, -3, -1, -10, 6]
def rearrange_array(nums):
    pos = []
    neg = []
    for i in nums:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)
    for i in range(0, len(pos)):
        nums[2*i] = pos[i]
        nums[2*i+1] = neg[i]

    print(nums)

rearrange_array(nums)

# Optimal Solution -> Time Complexity-> O(n), Space Complexity-> O(n)
nums = [5, 10, -3, -1, -10, 6]
result = [0] * len(nums)
p = 0
n = 1
for i in range(len(nums)):
    if nums[i]>=0:
        result[p] = nums[i]
        p += 2
    else:
        result[n] = nums[i]
        n += 2

print(result)