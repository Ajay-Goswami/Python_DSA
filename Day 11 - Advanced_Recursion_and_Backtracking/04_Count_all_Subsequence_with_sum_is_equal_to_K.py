# Count all Subsequences with sum is equal to K

# Input: arr = [1, 2, 1], K = 2
# Output: 2 (the subsequences are [1, 1] and [2])

def count_subsequences_with_sum_k(arr, k, index=0, current_sum=0): # O(2^n)
    # Base case: if we have considered all elements
    if index == len(arr):
        return 1 if current_sum == k else 0
    
    # Include the current element
    count_including = count_subsequences_with_sum_k(arr, k, index + 1, current_sum + arr[index])
    
    # Exclude the current element
    count_excluding = count_subsequences_with_sum_k(arr, k, index + 1, current_sum)
    
    return count_including + count_excluding

input_array = [1, 2, 1]
k_value = 2
result = count_subsequences_with_sum_k(input_array, k_value)
print(result)