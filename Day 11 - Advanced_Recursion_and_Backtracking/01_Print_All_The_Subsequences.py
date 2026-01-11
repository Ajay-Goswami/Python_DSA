# Print All the Subsequences of a String using Recursion

# Input: "abc"
# Output: ["", "a", "b", "c", "ab", "ac", "bc", "abc"]

def print_subsequences(s, index=0, current=""):
    # Base case: if we have considered all characters
    if index == len(s):
        print(current, end=' ')
        return
    
    # Include the current character
    print_subsequences(s, index + 1, current + s[index])
    
    # Exclude the current character
    print_subsequences(s, index + 1, current)


# Function to return all subsequences as a list
def subsequences_list(s, index=0, current="", result=None):
    if result is None:
        result = []
    
    # Base case: if we have considered all characters
    if index == len(s):
        result.append(current)
        return result
    
    # Include the current character
    subsequences_list(s, index + 1, current + s[index], result)
    
    # Exclude the current character
    subsequences_list(s, index + 1, current, result)
    
    return result


input_string = "abc"
print_subsequences(input_string)
subsequences_list_result = subsequences_list(input_string)
print("\nSubsequences List:", subsequences_list_result)
