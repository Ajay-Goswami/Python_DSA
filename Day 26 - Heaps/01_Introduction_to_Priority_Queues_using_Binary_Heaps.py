# Introduction to Priority Queues using Binary Heaps
# A Priority Queue is an abstract data type where each element has an associated priority.
# In a Max Heap, elements with higher priority are dequeued first.
# In a Min Heap, elements with lower priority are dequeued first.
# Binary Heaps are complete binary trees that satisfy the heap property.

# Example: Max Heap Priority Queue
# Priority Queue: [(5, 'Task A'), (3, 'Task B'), (7, 'Task C'), (1, 'Task D')]
# After dequeueing: (7, 'Task C') -> (5, 'Task A') -> (3, 'Task B') -> (1, 'Task D')


import heapq
from typing import Tuple, Optional

# Max Heap Priority Queue - higher priority values dequeue first
class MaxHeapPriorityQueue:
    """
    Max heap using heapq with negative priorities.
    Python's heapq is min-heap by default.
    """
    
    def __init__(self):
        self.heap = []
    
    def enqueue(self, priority: int, data: str) -> None:
        # O(log n) - Add element with priority.
        heapq.heappush(self.heap, (-priority, data))  # Store negative for max heap
    
    def dequeue(self) -> Optional[Tuple[int, str]]:
        # O(log n) - Remove and return highest priority element.
        if not self.heap:
            return None
        neg_priority, data = heapq.heappop(self.heap)
        return (-neg_priority, data)
    
    def peek(self) -> Optional[Tuple[int, str]]:
        # O(1) - View highest priority without removal.
        if not self.heap:
            return None
        neg_priority, data = self.heap[0]
        return (-neg_priority, data)
    
    def is_empty(self) -> bool:
        # O(1) - Check if empty.
        return len(self.heap) == 0
    
    def size(self) -> int:
        # O(1) - Get element count.
        return len(self.heap)


# Min Heap Priority Queue - lower priority values dequeue first
class MinHeapPriorityQueue:
    """
    Min heap priority queue using heapq directly.
    Lower priority numbers = higher urgency.
    """
    
    def __init__(self):
        self.heap = []
    
    def enqueue(self, priority: int, data: str) -> None:
        # O(log n) - Add element with priority.
        heapq.heappush(self.heap, (priority, data))
    
    def dequeue(self) -> Optional[Tuple[int, str]]:
        # O(log n) - Remove and return lowest priority element.
        if not self.heap:
            return None
        return heapq.heappop(self.heap)
    
    def peek(self) -> Optional[Tuple[int, str]]:
        # O(1) - View lowest priority without removal.
        if not self.heap:
            return None
        return self.heap[0]
    
    def is_empty(self) -> bool:
        # O(1) - Check if empty.
        return len(self.heap) == 0
    
    def size(self) -> int:
        # O(1) - Get element count.
        return len(self.heap)


# Demo both priority queues
if __name__ == "__main__":
    tasks = [(5, "Task A"), (3, "Task B"), (7, "Task C"), (1, "Task D")]
    
    print("Max Heap (higher priority first):")
    max_pq = MaxHeapPriorityQueue()
    for p, t in tasks:
        max_pq.enqueue(p, t)
    
    while not max_pq.is_empty():
        priority, task = max_pq.dequeue()
        print(f"Priority {priority}: {task}")
    
    print("\nMin Heap (lower priority first):")
    min_pq = MinHeapPriorityQueue()
    for p, t in tasks:
        min_pq.enqueue(p, t)
    
    while not min_pq.is_empty():
        priority, task = min_pq.dequeue()
        print(f"Priority {priority}: {task}")