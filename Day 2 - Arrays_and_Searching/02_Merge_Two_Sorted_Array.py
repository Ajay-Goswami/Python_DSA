# Merge Two Sorted Array and Duplicates are not allowed

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

nums1 = [1,2,3,4,6,9]
nums2 = [2,5,6]

def merge(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    i , j = 0, 0
    result = []
    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1
    while i<n:
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    while j<m:
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1
    return result

print(merge(nums1, nums2))