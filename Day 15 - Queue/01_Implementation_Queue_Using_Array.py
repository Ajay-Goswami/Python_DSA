# Implementation of a Queue using an Array (List in Python)

class Queue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Queue capacity must be greater than 0")

        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue Overflow")

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow")

        item = self.queue[self.front]
        self.queue[self.front] = None  # optional but clean
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            return []

        elements = []
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            elements.append(self.queue[index])
        return elements

    
if __name__ == "__main__":
    q = Queue(5)
    print(q.enqueue(10))
    print(q.enqueue(20))
    print(q.enqueue(30))
    print("Front element is:", q.peek())
    print("Queue elements:", q.display())
    print("Dequeued element:", q.dequeue())
    print("Queue elements after dequeue:", q.display())