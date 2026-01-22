# Bit Manipulation - A Bit Manipulation is a technique used to perform operations on individual bits of binary numbers.
# It involves manipulating the individual bits of a number to perform various operations such as setting, clearing, or toggling bits.


# Interger to Binary Conversion:
num = 10
binary_representation = bin(num)
print(binary_representation)  # Output: 0b1010

def int_to_binary(n):
    result = ''
    if n == 0:
        return '0'
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result
print(int_to_binary(10))  # Output: 1010

# Binary to Integer Conversion:
binary_str = '1010'
decimal_representation = int(binary_str, 2)
print(decimal_representation)  # Output: 10

def binary_to_int(b):
    result = 0
    power = 0
    for digit in reversed(b):
        result += int(digit) * (2 ** power)
        power += 1
    return result
print(binary_to_int('1010'))  # Output: 10



# 1's Complement: The 1's complement of a binary number is obtained by flipping all the bits (changing 0s to 1s and 1s to 0s).
def ones_complement(b):
    result = ''
    for bit in b:
        if bit == '0':
            result += '1'
        else:
            result += '0'
    return result
print(ones_complement('1010'))  # Output: 0101

# 2's Complement: The 2's complement of a binary number is obtained by taking the 1's complement and adding 1 to the least significant bit (LSB).
def twos_complement(b):
    ones_comp = ones_complement(b)
    n = len(ones_comp)
    result = list(ones_comp)
    
    carry = 1
    for i in range(n - 1, -1, -1):
        if ones_comp[i] == '1' and carry == 1:
            result[i] = '0'
        elif ones_comp[i] == '0' and carry == 1:
            result[i] = '1'
            carry = 0
        else:
            result[i] = ones_comp[i]
    
    return ''.join(result)
print(twos_complement('1010'))  # Output: 0110



# Basic Bitwise Operators in Python:
a = 5  # In binary: 0101
b = 3  # In binary: 0011

# 1. AND (&): The AND operator compares each bit of two numbers and returns 1 if both bits are 1, otherwise returns 0.
result = a & b  # In binary: 0001
print(result)  # Output: 1

# 2. OR (|): The OR operator compares each bit of two numbers and returns 1 if at least one of the bits is 1, otherwise returns 0.
result = a | b  # In binary: 0111
print(result)  # Output: 7

# 3. XOR (^): The XOR operator compares each bit of two numbers and returns 1 if the bits are different, otherwise returns 0.
result = a ^ b  # In binary: 0110
print(result)  # Output: 6

# 4. NOT (~): The NOT operator inverts the bits of a number, changing 1s to 0s and 0s to 1s.
result = ~a  # In binary: 1010 (two's complement representation)
print(result)  # Output: -6

# 5. Left Shift (<<): The left shift operator shifts the bits of a number to the left by a specified number of positions, filling the rightmost bits with 0s.
result = a << 1  # In binary: 1010
print(result)  # Output: 10

# 6. Right Shift (>>): The right shift operator shifts the bits of a number to the right by a specified number of positions, filling the leftmost bits with 0s for positive numbers and 1s for negative numbers.
result = a >> 1  # In binary: 0010
print(result)  # Output: 2


#Note:
# Right Shift -> x>>k : Divides x by 2^k
# Left Shift -> x<<k : Multiplies x by 2^k