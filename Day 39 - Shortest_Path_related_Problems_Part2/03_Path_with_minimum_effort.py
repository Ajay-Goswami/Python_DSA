# 03. Path With Minimum Effort
# Graph + Dijkstra's Algorithm (Priority Queue)

# Problem: Given a 2D grid of heights, find a path from top-left to bottom-right
# that minimizes the maximum absolute difference in heights between adjacent cells.

# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2

# Explanation: Use Dijkstra's algorithm where the "distance" is the maximum absolute
# difference along the path. The priority queue always processes the path with the
# smallest effort first, guaranteeing optimal result.

import heapq

def minimumEffortPath(heights): #O(n * m * log(n * m))
    n = len(heights)
    m = len(heights[0])

    effort = [[float('inf')] * m for _ in range(n)]
    effort[0][0] = 0

    pq = [(0, 0, 0)]  # (effort, row, col)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        e, r, c = heapq.heappop(pq)

        if r == n - 1 and c == m - 1:
            return e

        if e > effort[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m:
                newEffort = max(e, abs(heights[nr][nc] - heights[r][c]))

                if newEffort < effort[nr][nc]:
                    effort[nr][nc] = newEffort
                    heapq.heappush(pq, (newEffort, nr, nc))

    return effort[n - 1][m - 1]


heights = [
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5]
]

print(minimumEffortPath(heights))
