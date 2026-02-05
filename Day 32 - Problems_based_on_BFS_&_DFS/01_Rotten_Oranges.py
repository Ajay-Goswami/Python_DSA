# Rotten_Oranges

# Find minimum time to rot all oranges using BFS – LeetCode 994

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4


from collections import deque

def oranges_rotting(grid):  # O(m*n)
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    time = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue and fresh > 0:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        time += 1

    return time if fresh == 0 else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(oranges_rotting(grid))