# Next Greater Element II || Circular Array | Leetcode 503

# Input: nums = [1,2,1]
# Output: [2,-1,2]

def next_greater_elements(nums):
    n = len(nums)
    stack = []              # stores indices
    result = [-1] * n
    for i in range(2 * n):
        curr_index = i % n
        while stack and nums[stack[-1]] < nums[curr_index]:
            result[stack.pop()] = nums[curr_index]
        # push index only in first pass
        if i < n:
            stack.append(curr_index)
    return result

nums = [1, 2, 1]
print(next_greater_elements(nums))   # [2, -1, 2]
