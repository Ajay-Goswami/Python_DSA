# Heapify Algorithm - Transform an array into a valid heap structure
# Heapify operation restores the heap property for a node that may violate it.
# There are two types: Swim (Up) and Sink (Down)
# Time Complexity: O(log n) for single heapify operation

# Example: Heapify Down (Max Heap)
# Input: [10, 5, 3, 2, 8], index = 0
# After heapify: [10, 8, 3, 2, 5]


from typing import List

class Heapify:
    """
    Heapify operations for maintaining heap properties.
    Heapify-down (sink): Fixes violations moving down. O(log n)
    Heapify-up (swim): Fixes violations moving up. O(log n)
    """
    
    @staticmethod
    def heapify_down_max(arr: List[int], i: int, n: int) -> None:
        # O(log n) - Restore max heap by sinking element down.
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
            
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            Heapify.heapify_down_max(arr, largest, n)
    
    @staticmethod
    def heapify_down_min(arr: List[int], i: int, n: int) -> None:
        # O(log n) - Restore min heap by sinking element down.
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
            
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            Heapify.heapify_down_min(arr, smallest, n)
    
    @staticmethod
    def heapify_up_max(arr: List[int], i: int) -> None:
        # O(log n) - Restore max heap by swimming element up.
        while i > 0:
            parent = (i - 1) // 2
            if arr[parent] < arr[i]:
                arr[parent], arr[i] = arr[i], arr[parent]
                i = parent
            else:
                break
    
    @staticmethod
    def heapify_up_min(arr: List[int], i: int) -> None:
        # O(log n) - Restore min heap by swimming element up.
        while i > 0:
            parent = (i - 1) // 2
            if arr[parent] > arr[i]:
                arr[parent], arr[i] = arr[i], arr[parent]
                i = parent
            else:
                break


# Example usage
if __name__ == "__main__":
    # Max heap examples
    print("Max heap operations:")
    
    arr = [10, 5, 3, 2, 8]
    print(f"Before heapify_down: {arr}")
    Heapify.heapify_down_max(arr, 0, len(arr))
    print(f"After heapify_down:  {arr}")
    
    arr = [10, 5, 3, 2, 8]
    print(f"\nBefore heapify_up:   {arr}")
    Heapify.heapify_up_max(arr, 4)
    print(f"After heapify_up:    {arr}")
    
    # Min heap examples
    print("\nMin heap operations:")
    
    arr = [1, 5, 3, 10, 8]
    print(f"Before heapify_down: {arr}")
    Heapify.heapify_down_min(arr, 0, len(arr))
    print(f"After heapify_down:  {arr}")
    
    arr = [1, 5, 3, 10, 8]
    print(f"\nBefore heapify_up:   {arr}")
    Heapify.heapify_up_min(arr, 4)
    print(f"After heapify_up:    {arr}")