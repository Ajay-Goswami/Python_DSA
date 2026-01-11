# Find all subsequences in an array whose sum is equal to a given value K

# Input: arr = [1, 2, 1], K = 2
# Output: [[1, 1], [2]]


def find_subsequences_with_sum_k(arr, k, index=0, current=None, current_sum=0, result=None):
    if current is None:
        current = []
    if result is None:
        result = []
    
    # Base case: if we have considered all elements
    if index == len(arr):
        if current_sum == k:
            result.append(current.copy())
        return result
    
    # Include the current element
    current.append(arr[index])
    find_subsequences_with_sum_k(arr, k, index + 1, current, current_sum + arr[index], result)
    
    # Exclude the current element
    current.pop()
    find_subsequences_with_sum_k(arr, k, index + 1, current, current_sum, result)
    
    return result

input_array = [1, 2, 1]
k_value = 2
result = find_subsequences_with_sum_k(input_array, k_value)
print(result)