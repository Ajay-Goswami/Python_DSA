# 02. Shortest Path in a Binary Maze
# Graph + BFS (0-1 BFS / Level-order)

# Problem: Given an n x m binary grid where 1 means passable and 0 means blocked,
# find the shortest path from source to destination moving in 4 directions (up, down, left, right).

# Input: grid = [[1,1,1,1],[1,1,0,1],[1,1,1,1],[1,1,0,0],[1,0,0,1]], src = (0,1), dest = (2,2)
# Output: 3

# Explanation: Use BFS from source cell. Each cell is visited with the minimum distance.
# Since all edge weights are 1, BFS guarantees shortest path in an unweighted graph.

from collections import deque

def shortestPathBinaryMaze(grid, src, dest): #O(n * m)
    n = len(grid)
    m = len(grid[0])

    # Edge case
    if grid[src[0]][src[1]] == 0 or grid[dest[0]][dest[1]] == 0:
        return -1

    if src == dest:
        return 0

    dist = [[float('inf')] * m for _ in range(n)]
    dist[src[0]][src[1]] = 0

    q = deque([(0, src[0], src[1])])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        d, r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                if d + 1 < dist[nr][nc]:
                    dist[nr][nc] = d + 1

                    if (nr, nc) == dest:
                        return dist[nr][nc]

                    q.append((d + 1, nr, nc))

    return -1


grid = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 0, 1]
]
src = (0, 1)
dest = (2, 2)

print(shortestPathBinaryMaze(grid, src, dest))
