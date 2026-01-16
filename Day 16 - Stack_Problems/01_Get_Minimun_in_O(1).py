# Get Minimum in O(1) || Stack with Auxiliary Stack | Leetcode 155

# Input : ["MinStack","push","push","push","getMin","pop","top","getMin"]
#        : [[],[-2],[0],[-3],[],[],[],[]]
# Output : [null,null,null,null,-3,null,0,-2]

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val:int) -> None:
        self.stack.append(val)
        # If min_stack is empty or the new value is smaller or equal to the current minimum, push it onto min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # If the popped value is the current minimum, pop it from min_stack as well
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
    
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None
    

# example usage:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Output: -3
min_stack.pop()
print(min_stack.top())  # Output: 0
print(min_stack.getMin())  # Output: -2