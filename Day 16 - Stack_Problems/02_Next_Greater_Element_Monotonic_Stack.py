# Next Greater Element || Monotonic Stack | Leetcode 496

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]

def next_greater_element(nums1, nums2):
    stack = []
    result = [-1] * len(nums1)

    for i in range(len(nums2)-1, -1, -1):
        while stack and stack[-1] <= nums2[i]:
            stack.pop()
        if nums2[i] in nums1:
            index = nums1.index(nums2[i])
            if stack:
                result[index] = stack[-1]
        stack.append(nums2[i])

    return result

nums1 = [4,1,2] 
nums2 = [1,3,4,2]
print(next_greater_element(nums1, nums2))  # Output: [-1,3,-1]