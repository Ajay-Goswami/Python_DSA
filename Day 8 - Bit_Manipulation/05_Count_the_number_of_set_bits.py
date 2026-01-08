# Count the number of set bits in a given integer


def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1  # Increment count if the least significant bit is 1
        n = n >> 1      # Right shift n to check the next bit
    return count

number = 29  # Binary representation is 11101, which has 4 set bits
set_bits_count = count_set_bits(number)
print(f"Number of set bits in {number}: {set_bits_count}")  # Output: 4