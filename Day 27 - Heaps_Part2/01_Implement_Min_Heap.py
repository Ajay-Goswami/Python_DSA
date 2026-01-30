# Implement Min Heap
# A Min Heap is a complete binary tree where each parent node is smaller than its children.
# Minimum element is always at the root (index 0).
# Useful for priority queues, Dijkstra's algorithm, and heap sort.

# Example: Min Heap
# Insert: 5, 3, 10, 1, 7
# Structure: [1, 3, 10, 5, 7]
# Root (minimum) = 1


from typing import List

class MinHeap:
    
    def __init__(self): # O(1)
        self.heap = []
    
    def _swap(self, i: int, j: int): #  O(1)
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _parent(self, index: int) -> int: # O(1)
        return (index - 1) // 2
    
    def _left_child(self, index: int) -> int: # O(1)
        return 2 * index + 1
    
    def _right_child(self, index: int) -> int: # O(1)
        return 2 * index + 2
    
    def _heapify_up(self, index: int):
        # Move element up to restore min heap — O(log n)
        while index > 0:
            parent = self._parent(index)
            if self.heap[parent] > self.heap[index]:
                self._swap(parent, index)
                index = parent
            else:
                break
    
    def _heapify_down(self, index: int):
        # Move element down to restore min heap — O(log n)
        n = len(self.heap)
        while True:
            smallest = index
            left = self._left_child(index)
            right = self._right_child(index)
            
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break
    
    def insert(self, value: int): # O(log n)
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_min(self) -> int:
        # Remove and return minimum element — O(log n)
        if not self.heap:
            raise IndexError("Heap is empty")
        
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if self.heap:
            self._heapify_down(0)
        
        return min_val
    
    def get_min(self) -> int:
        # Return minimum without removing — O(1)
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def is_empty(self) -> bool: # O(1)
        return len(self.heap) == 0
    
    def size(self) -> int: # O(1)
        return len(self.heap)
    
    def display(self) -> List[int]: # O(n)
        return self.heap.copy()


# Example usage
if __name__ == "__main__":
    min_heap = MinHeap()
    
    values = [5, 3, 10, 1, 7, 15, 12]
    for val in values:
        min_heap.insert(val)
    
    print("Heap:", min_heap.display())
    print("Min:", min_heap.get_min())
    
    print("Extracting:")
    while not min_heap.is_empty():
        print(min_heap.extract_min(), end=" ")