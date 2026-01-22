# Find the number that appears odd number of times in an array

# Input : arr = [1, 2, 3, 2, 3, 1, 3]
# Output : 3

def findOddOccurrence(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

arr = [1, 2, 3, 2, 3, 1, 3]
print(findOddOccurrence(arr))