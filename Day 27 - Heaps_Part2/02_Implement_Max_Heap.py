# Implement Max Heap
# A Max Heap is a complete binary tree where each parent node is larger than its children.
# Maximum element is always at the root (index 0).
# Useful for heap sort, selection problems, and finding k largest elements.

# Example: Max Heap
# Insert: 5, 3, 10, 1, 7
# Structure: [10, 7, 5, 1, 3]
# Root (maximum) = 10

from typing import List

class MaxHeap:
    
    def __init__(self):  # O(1)
        self.heap = []
    
    def _swap(self, i: int, j: int):  # O(1)
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _parent(self, index: int) -> int:  # O(1)
        return (index - 1) // 2
    
    def _left_child(self, index: int) -> int:  # O(1)
        return 2 * index + 1
    
    def _right_child(self, index: int) -> int:  # O(1)
        return 2 * index + 2
    
    def _heapify_up(self, index: int):
        # Move element up to restore max heap — O(log n)
        while index > 0:
            parent = self._parent(index)
            if self.heap[parent] < self.heap[index]:
                self._swap(parent, index)
                index = parent
            else:
                break
    
    def _heapify_down(self, index: int):
        # Move element down to restore max heap — O(log n)
        n = len(self.heap)
        while True:
            largest = index
            left = self._left_child(index)
            right = self._right_child(index)
            
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            
            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break
    
    def insert(self, value: int):  # O(log n)
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_max(self) -> int:
        # Remove and return maximum element — O(log n)
        if not self.heap:
            raise IndexError("Heap is empty")
        
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if self.heap:
            self._heapify_down(0)
        
        return max_val
    
    def get_max(self) -> int:
        # Return maximum without removing — O(1)
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def is_empty(self) -> bool:  # O(1)
        return len(self.heap) == 0
    
    def size(self) -> int:  # O(1)
        return len(self.heap)
    
    def display(self) -> List[int]:  # O(n)
        return self.heap.copy()


# Example usage
if __name__ == "__main__":
    max_heap = MaxHeap()
    
    values = [5, 3, 10, 1, 7, 15, 12]
    for val in values:
        max_heap.insert(val)
    
    print("Heap:", max_heap.display())
    print("Max:", max_heap.get_max())
    
    print("Extracting:")
    while not max_heap.is_empty():
        print(max_heap.extract_max(), end=" ")