# Leetcode 242 : Valid Anagram

# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

s = "anagram"
t = "nagaram"

# Brute Force -> Time Complexity -> O(nlogn), Space Complexity -> O(1)
def isAnagram(s,t)->bool:
    return sorted(s) == sorted(t)

# Optimal Solution -> Time Complexity -> O(n), Space Complexity -> O(1)
def isAnagram(s,t)->bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for i in s:
        count[ord(i) - ord('a')] += 1
    for i in t:
        count[ord(i) - ord('a')] -= 1
    for i in count:
        if i != 0:
            return False
    return True