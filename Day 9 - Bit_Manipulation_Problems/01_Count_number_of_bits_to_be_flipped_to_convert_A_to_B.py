# Count the number of bits to be flipped to convert A to B

# Input : Start = 10, Goal = 7
# Output : 3
# Explanation: 10->1010
#              7-> 0111
#              3 bits to be flipped

def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def countBitsToBeFlipped(a, b):
    # XOR of a and b will give the bits that are different
    xor = a ^ b
    # Count the set bits in the XOR result
    return countSetBits(xor)

a = 10
b = 7
print("Number of bits to be flipped to convert", a, "to", b, "is:", countBitsToBeFlipped(a, b))
# Time Complexity: O(log n), where n is the maximum of a and b