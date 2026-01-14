# Reverse String Using Stack

def reverse_string(input_string):
    # Create a stack to hold characters
    stack = []
    
    # Push all characters of the string onto the stack
    for char in input_string:
        stack.append(char)
    
    # Pop all characters from the stack to get the reversed string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

str = "Hello, World!"
reversed_str = reverse_string(str)
print(reversed_str)