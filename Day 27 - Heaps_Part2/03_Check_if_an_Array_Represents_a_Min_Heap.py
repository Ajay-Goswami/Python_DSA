# Check if an Array Represents a Min Heap
# Validate whether an array satisfies the Min Heap property.
# In a Min Heap, each parent node must be smaller than or equal to its children.
# For node at index i: arr[i] <= arr[2*i+1] and arr[i] <= arr[2*i+2]

# Example:
# Input: [1, 2, 3, 4, 5, 6, 7]
# Output: True (Valid Min Heap)

# Input: [2, 1, 3]
# Output: False (Not a Min Heap, 2 > 1)


# Check if an Array Represents a Min Heap
# Each parent must be <= its children

from typing import List

class MinHeapValidator:
    
    @staticmethod
    def is_min_heap_recursive(arr: List[int], index: int = 0) -> bool:
        # Validate min heap using recursion — O(n) time, O(log n) space
        n = len(arr)
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < n:
            if arr[index] > arr[left]:
                return False
            if not MinHeapValidator.is_min_heap_recursive(arr, left):
                return False
        
        if right < n:
            if arr[index] > arr[right]:
                return False
            if not MinHeapValidator.is_min_heap_recursive(arr, right):
                return False
        
        return True
    
    @staticmethod
    def is_min_heap_iterative(arr: List[int]) -> bool:
        # Validate min heap using iteration — O(n) time, O(1) space
        n = len(arr)
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[i] > arr[left]:
                return False
            if right < n and arr[i] > arr[right]:
                return False
        
        return True
    
    @staticmethod
    def is_min_heap_oneline(arr: List[int]) -> bool:
        # One-line min heap check — O(n) time, O(1) space
        n = len(arr)
        return all(
            (arr[i] <= arr[2*i+1] if 2*i+1 < n else True) and
            (arr[i] <= arr[2*i+2] if 2*i+2 < n else True)
            for i in range(n // 2)
        )
    
    @staticmethod
    def validate_and_report(arr: List[int]) -> dict:
        # Validate heap and report violations — O(n)
        is_valid = MinHeapValidator.is_min_heap_iterative(arr)
        violations = []
        n = len(arr)
        
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[i] > arr[left]:
                violations.append(f"arr[{i}] > arr[{left}]")
            if right < n and arr[i] > arr[right]:
                violations.append(f"arr[{i}] > arr[{right}]")
        
        return {
            "is_valid": is_valid,
            "violations": violations
        }


# Example usage
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    print(arr1, "->", MinHeapValidator.is_min_heap_iterative(arr1))
    
    arr2 = [2, 1, 3]
    print(arr2, "->", MinHeapValidator.is_min_heap_iterative(arr2))
    print("Report:", MinHeapValidator.validate_and_report(arr2))
    
    arr3 = [5, 10, 15, 20, 25, 30, 35]
    print(arr3, "->", MinHeapValidator.is_min_heap_iterative(arr3))