# Prefix, Postfix, and Infix Notations (BASICS ONLY)

# 1. INFIX NOTATION
# Definition:
# In infix notation, the operator is placed BETWEEN the operands.
# This is the most common notation used in mathematics and programming.

# Example:
# a + b

# Python Example:
a = 5
b = 10

result_infix = a + b
print("Infix Result:", result_infix)   # Output: 15


# 2. POSTFIX NOTATION (Reverse Polish Notation)
# Definition:
# In postfix notation, the operator is placed AFTER the operands.

# Example:
# a b +
# 5 10 +

# Note:
# Python does NOT support postfix notation directly,
# so we simulate it using a stack.

# Python Simulation:
stack = []

# Push operands
stack.append(5)
stack.append(10)

# Pop operands
b = stack.pop()
a = stack.pop()

# Apply operator
stack.append(a + b)

# Final result
result_postfix = stack.pop()
print("Postfix Result:", result_postfix)   # Output: 15


# 3. PREFIX NOTATION
# Definition:
# In prefix notation, the operator is placed BEFORE the operands.

# Example:
# + a b
# + 5 10

# Note:
# Python does NOT support prefix notation directly,
# so we evaluate it manually.

# Python Simulation:
operator = "+"
a = 5
b = 10

if operator == "+":
    result_prefix = a + b

print("Prefix Result:", result_prefix)   # Output: 15


# FINAL SUMMARY
# Infix   : a + b
# Prefix  : + a b
# Postfix : a b +
#
# All give the same result: 15
