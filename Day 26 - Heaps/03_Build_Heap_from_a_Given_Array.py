# Build Heap from a Given Array
# Convert an unordered array into a valid heap structure.
# This is done by calling heapify on all non-leaf nodes in reverse order.
# Time Complexity: O(n) - Linear time heap construction

# Example: Build Max Heap from array
# Input: [4, 10, 3, 5, 1]
# Output: [10, 5, 3, 4, 1] (Valid Max Heap)


from typing import List

class HeapBuilder:
    """
    Build heaps from unordered arrays in O(n) time.
    Builds heap by heapifying non-leaf nodes in reverse order.
    """
    
    @staticmethod
    def _heapify_down_max(arr: List[int], i: int, n: int) -> None:
        # O(log n) - Sink element to maintain max heap.
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
            
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            HeapBuilder._heapify_down_max(arr, largest, n)
    
    @staticmethod
    def _heapify_down_min(arr: List[int], i: int, n: int) -> None:
        # O(log n) - Sink element to maintain min heap.
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
            
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            HeapBuilder._heapify_down_min(arr, smallest, n)
    
    @staticmethod
    def build_max_heap(arr: List[int]) -> List[int]:
        # O(n) - Build max heap in-place.
        n = len(arr)
        # Start from last non-leaf node: index = (n//2) - 1
        for i in range(n // 2 - 1, -1, -1):
            HeapBuilder._heapify_down_max(arr, i, n)
        return arr
    
    @staticmethod
    def build_min_heap(arr: List[int]) -> List[int]:
        # O(n) - Build min heap in-place.
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            HeapBuilder._heapify_down_min(arr, i, n)
        return arr
    
    @staticmethod
    def is_max_heap(arr: List[int]) -> bool:
        # O(n) - Validate max heap property.
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
        # O(n) - Validate min heap property.
        n = len(arr)
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[i] > arr[left]:
                return False
            if right < n and arr[i] > arr[right]:
                return False
        return True


# Test the heap builder
if __name__ == "__main__":
    test_cases = [
        [4, 10, 3, 5, 1],
        [15, 10, 20, 8, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]
    
    for arr in test_cases:
        print(f"\nOriginal: {arr}")
        
        max_heap = arr.copy()
        HeapBuilder.build_max_heap(max_heap)
        print(f"Max heap: {max_heap} (valid: {HeapBuilder.is_max_heap(max_heap)})")
        
        min_heap = arr.copy()
        HeapBuilder.build_min_heap(min_heap)
        print(f"Min heap: {min_heap} (valid: {HeapBuilder.is_min_heap(min_heap)})")