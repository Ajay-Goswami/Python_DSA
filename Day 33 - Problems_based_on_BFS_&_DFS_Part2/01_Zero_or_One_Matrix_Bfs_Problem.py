# Zero_or_One_Matrix_Bfs_Problem

# Distance of nearest zero using BFS – LeetCode 542

# Input: mat =[[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]


from collections import deque

def update_matrix(mat):  # O(m*n)
    rows, cols = len(mat), len(mat[0])
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                queue.append((r, c))
            else:
                mat[r][c] = -1

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                mat[nr][nc] = mat[r][c] + 1
                queue.append((nr, nc))

    return mat


mat = [[0,0,0],[0,1,0],[1,1,1]]
print(update_matrix(mat))