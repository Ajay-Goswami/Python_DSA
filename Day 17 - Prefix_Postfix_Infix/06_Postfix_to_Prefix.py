# Postfix to Prefix Conversion

# Input : a = "ABCD^E-*+"
# Output: a = "+A*B^-CDE"

def postfix_to_prefix(expression):
    stack = []

    for char in expression:
        if char.isalpha():
            stack.append(char)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(char + a + b)

    return stack.pop()


# Example usage
postfix_expression = "ABCD^E-*+"
prefix_expression = postfix_to_prefix(postfix_expression)
print("Prefix Expression:", prefix_expression)
