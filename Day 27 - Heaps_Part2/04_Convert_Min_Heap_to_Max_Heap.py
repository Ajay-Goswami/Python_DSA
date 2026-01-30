# Convert Min Heap to Max Heap
# Transform a Min Heap into a Max Heap by reordering elements.
# In Min Heap: parent <= children. In Max Heap: parent >= children.
# Approach: Build a Max Heap from the array using heapify operation.
# Time Complexity: O(n)

# Example:
# Input Min Heap: [1, 2, 3, 4, 5, 6, 7]
# Output Max Heap: [7, 5, 6, 4, 2, 1, 3] or similar valid Max Heap


# Convert Min Heap to Max Heap
# Reorder elements to satisfy Max Heap property

from typing import List

class HeapConverter:
    
    @staticmethod
    def heapify_down_max(arr: List[int], index: int, n: int):
        # Restore max heap by moving element down — O(log n)
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != index:
            arr[index], arr[largest] = arr[largest], arr[index]
            HeapConverter.heapify_down_max(arr, largest, n)
    
    @staticmethod
    def heapify_down_min(arr: List[int], index: int, n: int):
        # Restore min heap by moving element down — O(log n)
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        
        if smallest != index:
            arr[index], arr[smallest] = arr[smallest], arr[index]
            HeapConverter.heapify_down_min(arr, smallest, n)
    
    @staticmethod
    def min_heap_to_max_heap(arr: List[int]) -> List[int]:
        # Convert min heap to max heap — O(n)
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            HeapConverter.heapify_down_max(arr, i, n)
        return arr
    
    @staticmethod
    def max_heap_to_min_heap(arr: List[int]) -> List[int]:
        # Convert max heap to min heap — O(n)
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            HeapConverter.heapify_down_min(arr, i, n)
        return arr
    
    @staticmethod
    def is_max_heap(arr: List[int]) -> bool:
        # Check if array is max heap — O(n)
        n = len(arr)
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[i] < arr[left]:
                return False
            if right < n and arr[i] < arr[right]:
                return False
        return True
    
    @staticmethod
    def is_min_heap(arr: List[int]) -> bool:
        # Check if array is min heap — O(n)
        n = len(arr)
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[i] > arr[left]:
                return False
            if right < n and arr[i] > arr[right]:
                return False
        return True


# Example usage
if __name__ == "__main__":
    min_heap = [1, 2, 3, 4, 5, 6, 7]
    print("Min Heap:", min_heap)
    print("Is Min Heap:", HeapConverter.is_min_heap(min_heap))
    
    max_heap = HeapConverter.min_heap_to_max_heap(min_heap.copy())
    print("Converted Max Heap:", max_heap)
    print("Is Max Heap:", HeapConverter.is_max_heap(max_heap))
    
    max_heap = [7, 6, 5, 4, 1, 2, 3]
    print("\nMax Heap:", max_heap)
    print("Is Max Heap:", HeapConverter.is_max_heap(max_heap))
    
    min_heap = HeapConverter.max_heap_to_min_heap(max_heap.copy())
    print("Converted Min Heap:", min_heap)
    print("Is Min Heap:", HeapConverter.is_min_heap(min_heap))