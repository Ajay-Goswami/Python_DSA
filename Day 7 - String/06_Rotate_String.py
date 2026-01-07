# Leetcode 796 : Rotate String

# Input: s = "abcde", goal = "cdeab"
# Output: true

# Input: s = "abcde", goal = "abced"
# Output: false

s = "abcde"
goal = "cdeab"

def rotateString(s, goal)->bool:
    if len(s) != len(goal):
        return False
    return s in goal*2

print(rotateString(s, goal))