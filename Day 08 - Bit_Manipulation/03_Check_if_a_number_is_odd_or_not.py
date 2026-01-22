# Check if a number is odd or not

def is_odd(n):
    # A number is odd if its least significant bit (LSB) is 1
    return (n & 1) == 1

number = 7
odd_check = is_odd(number)
print(f"Is {number} odd? {odd_check}")  # Output: True