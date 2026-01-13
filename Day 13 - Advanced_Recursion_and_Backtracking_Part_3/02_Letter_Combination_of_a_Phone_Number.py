# Letter Combination of a Phone Number

# Input : digits = "23"
# Output : ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def letterCombinations(digits):
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index, path):
        if index == len(digits):
            result.append("".join(path))
            return
        
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    result = []
    backtrack(0, [])
    return result

digits1 = "23"
print(letterCombinations(digits1))