# Postfix to Infix Conversion

# Input : a = "ABCD^E-*+"
# Output: a = "A+B*(C^D-E)"

def postfix_to_infix(expression):
    stack = []

    for char in expression:
        if char.isalpha():
            stack.append(char)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(f"({a}{char}{b})")

    return stack.pop()


# Example usage
postfix_expression = "ABCD^E-*+"
infix_expression = postfix_to_infix(postfix_expression)
print("Infix Expression:", infix_expression)
