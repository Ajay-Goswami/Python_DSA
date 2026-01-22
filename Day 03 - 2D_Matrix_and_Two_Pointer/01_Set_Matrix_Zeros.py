# Set Matrix Zeros - Leetcode - 73 
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Input : matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output : [[1,0,1],[0,0,0],[1,0,1]]

matrix = [[0,1,1],[1,0,1],[1,1,1]]
m = len(matrix)
n = len(matrix[0])

# Brute Force - Using infinty marker -> Time Complexity-> O(m*n*(m+n)) -> Space Complexity-> O(1)
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            for col in range(n): # row
                if matrix[i][col] != 0:
                    matrix[i][col] = float('inf')
            for row in range(m): # col
                if matrix[row][j] != 0:
                    matrix[row][j] = float('inf')
for i in range(m):
    for j in range(n):
        if matrix[i][j] == float('inf'):
            matrix[i][j] = 0

print(matrix)


# Better Approach -> Using Extra Space -> Time Complexity - O(m*n), Space Complexity - O(m+n)
def set_zeros(matrix):
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in cols:
                matrix[i][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
set_zeros(matrix)
print(matrix)


# Optimal Approach -> Time Complexity - O(m*n), Space Complexity - O(1)
def set_matrix_zeros(matrix):
    n, m = len(matrix), len(matrix[0])
    col0 = 1
    for i in range(n): # mark first column and first row
        if matrix[i][0] == 0:
            col0 = 0
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, n): # Fill 0 in the matrix
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0: # lastly handle first column
        for j in range(m):
            matrix[0][j] = 0

    if col0 == 0: # lastly handle first row
        for i in range(n):
            matrix[i][0] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
set_matrix_zeros(matrix)
print(matrix)