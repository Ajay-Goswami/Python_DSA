# Power Set -> Print all Subsets

# Input : set = [1, 2, 3]
# Output : [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

# Note : The power set of a set with n elements has 2^n subsets.

def powerSet(input_set):
    n = len(input_set)
    subsets = []
    
    # There are 2^n subsets for a set of size n
    for i in range(2**n):
        subset = []
        for j in range(n):
            # Check if jth bit in i is set
            if (i & (1 << j)) > 0:
                subset.append(input_set[j])
        subsets.append(subset)
    
    return subsets

input_set = [1, 2, 3]
result = powerSet(input_set)
print(result)