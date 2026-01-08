# Check if the i-th bit is set in a given integer

def is_ith_bit_set(n, i):
    # Create a mask by left shifting 1 by i positions
    mask = 1 << i
    # Use bitwise AND to check if the i-th bit is set
    return (n & mask) != 0

is_set = is_ith_bit_set(5, 0)  # 5 in binary is 101, so the 0-th bit is set
print(f"Is the 0-th bit set in 5? {is_set}")
