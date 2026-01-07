# Leetcode 1021 : Remove Outermost Parentheses

# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: The String is "(()())(())", we delete the outermost parentheses to get "()()()".

# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"

# Input: s = "()()"
# Output: ""


s = "(()())(())(()(()))"

def removeOuterParentheses(s):
    count = 0
    res = ""
    for i in s:
        if i == "(":
            count += 1
            if count > 1:
                res += i
        elif i == ")":
            count -= 1
            if count > 0:
                res += i
    return res

print(removeOuterParentheses(s))