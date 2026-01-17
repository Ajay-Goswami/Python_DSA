# Prefix to Infix Conversion

# Input : a = "+A*B^-CDE"
# Output: a = "A+B*(C^D-E)"

def prefix_to_infix(expression):
    stack = []

    for char in reversed(expression):
        if char.isalpha():
            stack.append(char)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(f"({a}{char}{b})")

    return stack.pop()


# Example usage
prefix_expression = "+A*B^-CDE"
infix_expression = prefix_to_infix(prefix_expression)
print("Infix Expression:", infix_expression)
