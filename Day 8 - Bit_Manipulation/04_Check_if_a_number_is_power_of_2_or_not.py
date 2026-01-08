# Check if a number is power of 2 or not

def is_power_of_two(n):
    # A number is a power of 2 if it is greater than 0 and
    # the bitwise AND of the number and one less than the number is 0
    return n > 0 and (n & (n - 1)) == 0


number = 16
power_check = is_power_of_two(number)
print(f"Is {number} a power of 2? {power_check}")  # Output: True