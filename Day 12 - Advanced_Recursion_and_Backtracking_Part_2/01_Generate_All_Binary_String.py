# Generate All Binary Strings of Length N using Recursion

# Input: n = 3
# Output: ['000', '001', '010', '011', '100', '101', '110', '111']

def generate_binary_strings(n):
    def backtrack(current_string):
        if len(current_string) == n:
            result.append(current_string)
            return
        backtrack(current_string + '0')
        backtrack(current_string + '1')

    result = []
    backtrack('')
    return result

n = 3
result = generate_binary_strings(n)
print(result)