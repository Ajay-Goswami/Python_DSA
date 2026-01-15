# Implementation Stack using queue

from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        print("Pushed:", x)
        print("Stack state:", list(self.q))

    def pop(self):
        if not self.q:
            print("Stack Underflow")
            return
        val = self.q.popleft()
        print("Popped:", val)
        print("Stack state:", list(self.q))
        return val

    def top(self):
        if not self.q:
            print("Stack is empty")
            return
        print("Top element:", self.q[0])
        return self.q[0]

    def is_empty(self):
        print("Is stack empty?", len(self.q) == 0)
        return len(self.q) == 0


if __name__ == "__main__":
    s = StackUsingQueue()
    s.push(10)
    s.push(20)
    s.push(30)
    s.top()
    s.pop()
    s.pop()
    s.is_empty()
    s.pop()
    s.pop()
    s.is_empty()