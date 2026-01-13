# Rat in a Maze Problem using Backtracking

# Input: A 2D grid representing the maze (0 = open cell, 1 = blocked cell)
# Output: All possible paths from the top-left to the bottom-right corner

def ratInMaze(maze):
    n = len(maze)
    result = []
    visited = [[False]*n for _ in range(n)]

    def isSafe(x, y): # Check if cell is valid
        return 0 <= x < n and 0 <= y < n and maze[x][y] == 0 and not visited[x][y]

    def backtrack(x, y, path):
        if x == n - 1 and y == n - 1: # Destination reached
            result.append(path)
            return

        visited[x][y] = True
        if isSafe(x + 1, y): # Down
            backtrack(x + 1, y, path + "D")
        if isSafe(x, y + 1): # Right
            backtrack(x, y + 1, path + "R")
        if isSafe(x - 1, y): # Up
            backtrack(x - 1, y, path + "U")
        if isSafe(x, y - 1): # Left
            backtrack(x, y - 1, path + "L")
        visited[x][y] = False  # Backtrack

    if maze[0][0] == 0:
        backtrack(0, 0, "")

    return result

maze1 = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

print(ratInMaze(maze1))
