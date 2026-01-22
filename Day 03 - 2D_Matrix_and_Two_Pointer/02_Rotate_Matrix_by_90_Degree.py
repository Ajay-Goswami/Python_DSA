# Rotate Matrix by 90 Degree - Leetcode 48
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# Input : matrix = [[1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16]]
# Output : [[13,9,5,1],
#           [14,10,6,2],
#           [15,11,7,3],
#           [16,12,8,4]]

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix_2 = [[1,2,3,4,5],[5,6,7,8,9],[9,10,11,12,13],[13,14,15,16,17],[17,18,19,20,21]]

# Using Transpose + Reverse -> Time Complexity - O(n*n + n), Space Complexity - O(1)
def rotate(matrix):
    n= len(matrix)
    for i in range(n): # Transpose
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix: # Reverse each row
        row.reverse()
    print("Using Transpose + Reverse : ",matrix)


# Using 4 Pointers -> Time Complexity - O(n*n), Space Complexity - O(1)
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n//2):
        for j in range(i, n-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = temp
    print("Using 4 Pointers : ",matrix)


rotate(matrix)
rotate_matrix(matrix_2)