# Flood_Fill

# Fill connected pixels with new color using DFS – LeetCode 733

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]


def flood_fill(image, sr, sc, color):  # O(m*n)
    old_color = image[sr][sc]
    if old_color == color:
        return image

    rows, cols = len(image), len(image[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if image[r][c] != old_color:
            return
        image[r][c] = color
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(sr, sc)
    return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(flood_fill(image, sr, sc, color))