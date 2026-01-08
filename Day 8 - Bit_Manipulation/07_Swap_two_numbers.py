# Swap Two Numbers Without Using a Temporary Variable

def swap_numbers(a, b):
    print(f"Original values: a = {a}, b = {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"Swapped values: a = {a}, b = {b}")
    return a, b

swap_numbers(5, 10)  # Output: a = 10, b = 5