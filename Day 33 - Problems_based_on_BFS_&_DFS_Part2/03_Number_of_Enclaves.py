# Number_of_Enclaves - Leetcode 1020

# Count the number of enclaves in a matrix of 1s and 0s where 1 represents land and 0 represents water.
# A group of connected 1s forms an island. An island is said to be an enclave if it is surrounded by water on all sides except one side.
# Return the number of enclaves in the given matrix.

# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3

# Input: grid = [[0,0,0],[1,0,1],[1,1,1]]
# Output: 0

from collections import deque

def num_enclaves(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 0
                queue.append((nr, nc))

    return sum(sum(row) for row in grid)


grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(num_enclaves(grid))