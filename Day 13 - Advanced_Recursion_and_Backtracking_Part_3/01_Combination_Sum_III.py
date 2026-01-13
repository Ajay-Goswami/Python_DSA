# Combination Sum III

# Input : k = 3, n = 7
# Output : [[1,2,4]]

# Input : k = 3, n = 9
# Output : [[1,2,6], [1,3,5], [2,3,4]]

def combinationSum3(k, n):
    def backtrack(start, path, remaining_k, remaining_n):
        if remaining_k == 0 and remaining_n == 0:
            result.append(path)
            return
        if remaining_k < 0 or remaining_n < 0:
            return
        
        for i in range(start, 10):
            backtrack(i + 1, path + [i], remaining_k - 1, remaining_n - i)

    result = []
    backtrack(1, [], k, n)
    return result

k1, n1 = 3, 9
print(combinationSum3(k1, n1))