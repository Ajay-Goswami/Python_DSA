# Task Scheduler

# Leetcode - 621
# Given a list of tasks and a non-negative cooling interval n,
# find the least number of time units required to finish all tasks.
# Same tasks must be separated by at least n intervals.

# Input:  tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B

from collections import Counter
import heapq

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

# ----------------------------------------------------
# Optimal Approach using Max Heap + Greedy
# Time Complexity -> O(n log 26) ≈ O(n)
# Space Complexity -> O(1) (since max 26 tasks)
# ----------------------------------------------------
def least_interval(tasks, n):
    # Count frequency of each task
    freq = Counter(tasks)

    # Use max heap (negative values for Python)
    max_heap = [-count for count in freq.values()]
    heapq.heapify(max_heap)

    time = 0

    # Process tasks in cycles of (n + 1)
    while max_heap:
        temp = []
        cycle = n + 1

        while cycle > 0 and max_heap:
            count = heapq.heappop(max_heap)
            if count + 1 < 0:
                temp.append(count + 1)
            time += 1
            cycle -= 1

        # Push remaining tasks back to heap
        for item in temp:
            heapq.heappush(max_heap, item)

        # If heap is not empty, add idle time
        if max_heap:
            time += cycle

    return time


print("Least time required ->", least_interval(tasks, n))