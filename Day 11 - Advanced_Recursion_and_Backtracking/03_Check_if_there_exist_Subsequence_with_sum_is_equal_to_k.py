# Check if there exist a subsequence with sum equal to k in an array (using recursion and backtracking)

# Input: arr = [1, 2, 3], K = 5
# Output: True (because the subsequence [2, 3] sums to 5


def check_subsequence_with_sum_k(arr, k, index=0, current_sum=0): # O(2^n)
    # Base case: if we have considered all elements
    if index == len(arr):
        return current_sum == k
    
    # Include the current element
    if check_subsequence_with_sum_k(arr, k, index + 1, current_sum + arr[index]):
        return True
    
    # Exclude the current element
    if check_subsequence_with_sum_k(arr, k, index + 1, current_sum):
        return True
    
    return False
input_array = [1, 2, 3]
k_value = 5
result = check_subsequence_with_sum_k(input_array, k_value)
print(result)