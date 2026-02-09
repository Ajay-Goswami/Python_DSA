# 01. Number of Distinct Islands
# DFS Multisource Problem

# Problem: Given a 2D grid consisting of 0s (water) and 1s (land), return the number of DISTINCT islands.
# Two islands are considered distinct if their shapes are different.

# Input:
# grid = [
#   [1,1,0,0,0],
#   [1,0,0,0,0],
#   [0,0,0,1,1],
#   [0,0,0,1,1]
# ]

# Output: 2
# Explanation: First island shape is different from the second island shape.

def numDistinctIslands(grid): # O(m*n)
    rows, cols = len(grid), len(grid[0])
    shapes = set()

    def dfs(r, c, base_r, base_c, shape):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if grid[r][c] != 1:
            return

        grid[r][c] = 0
        shape.append((r - base_r, c - base_c))

        dfs(r + 1, c, base_r, base_c, shape)
        dfs(r - 1, c, base_r, base_c, shape)
        dfs(r, c + 1, base_r, base_c, shape)
        dfs(r, c - 1, base_r, base_c, shape)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                shape = []
                dfs(r, c, r, c, shape)
                shapes.add(tuple(shape))

    return len(shapes)


grid = [
    [1,1,0,0,0],
    [1,0,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
]
print(numDistinctIslands(grid))
