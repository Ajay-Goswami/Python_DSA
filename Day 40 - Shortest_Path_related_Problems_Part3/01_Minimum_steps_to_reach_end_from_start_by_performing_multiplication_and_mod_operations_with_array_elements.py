# 01. Minimum Steps to Reach End from Start by Performing Multiplication and Mod Operations
# Graph + BFS (Shortest Path in Unweighted Graph)

# Problem: Given start, end and an array of integers, find the minimum number of steps
# to reach end from start. In each step, you can multiply start by any element of the
# array and take mod with 100000 to get the new start. Find minimum steps to reach end.

# Input: arr = [2, 5, 7], start = 3, end = 30
# Output: 2

# Explanation: Step 1: 3 * 2 = 6 (mod 100000) -> 6
#              Step 2: 6 * 5 = 30 (mod 100000) -> 30 (reached end)
#              BFS guarantees the shortest path (minimum steps).

from collections import deque

def minSteps(arr, start, end): #O(100000 * N) where N = len(arr)
    MOD = 100000

    if start == end:
        return 0

    visited = [False] * MOD
    visited[start] = True

    queue = deque([(start, 0)])

    while queue:
        node, steps = queue.popleft()

        for num in arr:
            new_node = (node * num) % MOD

            if new_node == end:
                return steps + 1

            if not visited[new_node]:
                visited[new_node] = True
                queue.append((new_node, steps + 1))

    return -1


arr = [2, 5, 7]
start = 3
end = 30

result = minSteps(arr, start, end)
print(f"Minimum steps: {result}")
