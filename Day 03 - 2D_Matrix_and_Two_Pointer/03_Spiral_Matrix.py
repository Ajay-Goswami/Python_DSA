# Spiral Matrix -Leetcode 54
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Input : matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output : [1,2,3,6,9,8,7,4,5]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
m = len(matrix)
n = len(matrix[0])


def spiral_matrix(matrix):
    res = []
    left = 0
    right = n - 1
    top = 0
    bottom = m - 1
    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            res.append(matrix[top][col])
        for row in range(top + 1, bottom + 1):
            res.append(matrix[row][right])
        for col in reversed(range(left, right)):
            res.append(matrix[bottom][col])
        for row in reversed(range(top + 1, bottom)):
            res.append(matrix[row][left])
        left += 1
        right -= 1
        top += 1
        bottom -= 1
    return res

print(spiral_matrix(matrix))