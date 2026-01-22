# Leetcode 1614 : Maximum Nesting Depth of the Parentheses
# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3

# Input: s = "(1)+((2))+(((3)))"
# Output: 3

s = "(1+(2*3)+((8)/4))+1"

def maxDepth(s):
    current = 0
    max_depth = 0

    for ch in s:
        if ch == "(":
            current += 1
            max_depth = max(max_depth, current)
        elif ch == ")":
            current -= 1

    return max_depth

print(maxDepth(s))