# Check Valid  Parentheses using Stack

def is_valid_parentheses(s):
    # Create a stack to hold opening parentheses
    stack = []
    
    # Dictionary to hold matching pairs
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_parentheses.values():  # If it's an opening bracket
            stack.append(char)
        elif char in matching_parentheses.keys():  # If it's a closing bracket
            if not stack or stack[-1] != matching_parentheses[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

string = "{[()]}"
if is_valid_parentheses(string):
    print(f"The string '{string}' has valid parentheses.")
else:
    print(f"The string '{string}' does not have valid parentheses.")