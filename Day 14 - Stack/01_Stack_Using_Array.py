# Stack - It is a linear data structure that follows the LIFO (Last In First Out) principle.
# Insertion and deletion happen from only ONE end, called the TOP.

# Stack Implementation Using Array

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise Exception("Stack Overflow: Cannot push to a full stack.")
        self.stack.append(item)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow: Cannot pop from an empty stack.")
        item = self.stack.pop()
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty: Cannot peek.")
        return self.stack[self.top]

    def size(self):
        return self.top + 1

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements:", self.stack)

# Example usage:
if __name__ == "__main__":
    stack = Stack(5)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()  # Output: Stack elements: [10, 20, 30]
    print("Top element is:", stack.peek())  # Output: Top element is: 30
    print("Stack size is:", stack.size())  # Output: Stack size is: 3
    print("Popped element is:", stack.pop())  # Output: Popped element is: 30
    stack.display()  # Output: Stack elements: [10, 20]