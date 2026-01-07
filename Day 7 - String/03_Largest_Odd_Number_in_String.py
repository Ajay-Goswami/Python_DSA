# Leetcode 1903 : Largest Odd Number in String

# Input: num = "52"
# Output: "5"

# Input: num = "4206"
# Output: ""

# Input: num = "35427"
# Output: "35427"

# num = "35427"
num = "52"

def largestOddNumber(num):
    for i in range(len(num)-1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[:i+1]
    return ""

print(largestOddNumber(num))