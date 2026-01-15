# Implementation of a Queue using one stack

class QueueUsingOneStack:
    def __init__(self):
        self.stack = []

    def enqueue(self, x):
        self.stack.append(x)
        print("Enqueued:", x)
        print("Queue state:", self.display())

    def dequeue(self):
        if not self.stack:
            print("Queue Underflow")
            return

        if len(self.stack) == 1:
            val = self.stack.pop()
            print("Dequeued:", val)
            print("Queue state:", self.display())
            return val

        temp = self.stack.pop()
        val = self.dequeue()
        self.stack.append(temp)
        return val

    def display(self):
        return self.stack[::-1]


if __name__ == "__main__":
    q = QueueUsingOneStack()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(40)
    q.enqueue(50)
    q.display()