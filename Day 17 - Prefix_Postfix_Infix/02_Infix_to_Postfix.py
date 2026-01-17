# Infix to Postfix Conversion using Shunting Yard Algorithm

# Input : a = "A+B*(C^D-E)"
# Output: a = "ABCD^E-*+"

def infix_to_postfix(expression):
    precedence = {'^': 3, '*': 2, '/': 2, '%': 2, '+': 1, '-': 1}
    right_associative = {'^'}
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
            while (
                stack and stack[-1] != '(' and
                (
                    precedence[char] < precedence[stack[-1]] or
                    (precedence[char] == precedence[stack[-1]] and char not in right_associative)
                )
            ):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

# Example usage
infix_expression = "A+B*(C^D-E)"
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix Expression:", postfix_expression)
