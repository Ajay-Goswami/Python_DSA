# Leetcode 14 : Longest Common Prefix

# Input: strs = ["flower","flow","flight"]
# Output: "fl"


# Input: strs = ["dog","racecar","car"]
# Output: ""

strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    strs.sort()

    first = strs[0]
    last = strs[-1]
    res = ""
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            res += first[i]
        else:
            break

    return res

print("Longest Common Prefix ->", longestCommonPrefix(strs))