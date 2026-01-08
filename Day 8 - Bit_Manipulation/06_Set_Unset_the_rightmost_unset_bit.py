# Set/Unset the rightmost unset bit of a number

def set_rightmost_unset_bit(n):
    # To set the rightmost unset bit, we can use the expression n | (n + 1)
    return n | (n + 1)

def unset_rightmost_set_bit(n):
    # To unset the rightmost unset bit, we can use the expression n & (n + 1)
    return n & (n + 1)

number = 21  # Binary representation is 10101
new_number_set = set_rightmost_unset_bit(number)
new_number_unset = unset_rightmost_set_bit(number)
print(f"Original number: {number} (Binary: {bin(number)})")
print(f"After setting rightmost unset bit: {new_number_set} (Binary: {bin(new_number_set)})")
print(f"After unsetting rightmost unset bit: {new_number_unset} (Binary: {bin(new_number_unset)})")

