# Infix to Prefix Conversion using Reversal and Postfix Method

# Input : a = "A+B*(C^D-E)"
# Output: a = "+A*B^-CDE"

def infix_to_prefix(expression):
    precedence = {'^': 3, '*': 2, '/': 2, '%': 2, '+': 1, '-': 1}

    expression = expression[::-1]
    expression = ''.join('(' if c == ')' else ')' if c == '(' else c for c in expression)

    stack = []
    postfix = []

    for char in expression:
        if char.isalpha():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[char] < precedence[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix[::-1])


# Example usage
infix_expression = "A+B*(C^D-E)"
print("Prefix Expression:", infix_to_prefix(infix_expression))
