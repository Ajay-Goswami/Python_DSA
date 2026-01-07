# Leetcode 205 : Isomorphic Strings

# Input: s = "egg", t = "add"
# Output: true
# Explanation: String s and t can be made identical by changing mapping 'e' -> 'a' and 'g' -> 'd'.

# Input: s = "foo", t = "bar"
# Output: false

s = "egeg"
t = "adda"

def isIsomorphic(s, t):
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

print(isIsomorphic(s, t))