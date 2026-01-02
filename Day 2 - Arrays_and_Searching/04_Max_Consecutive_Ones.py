# Maximum Consecutive Once - 
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Input : nums = [1,1,0,1,1,1]
# Output : 3

nums = [1,1,0,1,1,1,0,1,1,1,1,0,0,1]
count = 0 
MaxCount = 0
for i in nums:
    if i == 1:
        count += 1
        MaxCount = max(MaxCount, count)
    else:
        count = 0
print(MaxCount)

def max_consecutive_ones(nums): # O(n)
    count = 0
    MaxCount = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            MaxCount = max(MaxCount, count)
            count = 0
    return max(MaxCount, count)

print(max_consecutive_ones(nums))