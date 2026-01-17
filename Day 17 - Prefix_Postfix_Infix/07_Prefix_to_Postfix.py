# Prefix to Postfix Conversion

# Input : a = "+A*B^-CDE"
# Output: a = "ABCD^E-*+"

def prefix_to_postfix(expression):
    stack = []

    for char in reversed(expression):
        if char.isalpha():
            stack.append(char)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b + char)

    return stack.pop()


# Example usage
prefix_expression = "+A*B^-CDE"
postfix_expression = prefix_to_postfix(prefix_expression)
print("Postfix Expression:", postfix_expression)
