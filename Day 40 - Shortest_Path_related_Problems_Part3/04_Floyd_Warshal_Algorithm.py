# 04. Floyd-Warshall Algorithm
# Graph + Dynamic Programming (All-Pairs Shortest Path)

# Problem: Given a weighted directed graph with V vertices represented as an
# adjacency matrix, find the shortest distances between every pair of vertices.
# The graph may contain negative edge weights but no negative weight cycles.
# Use -1 to represent no direct edge between two vertices.

# Input: matrix = [[0, 2, -1, 6],
#                   [-1, 0, 3, 8],
#                   [-1, -1, 0, 1],
#                   [-1, -1, -1, 0]]
# Output: [[0, 2, 5, 6],
#           [-1, 0, 3, 4],
#           [-1, -1, 0, 1],
#           [-1, -1, -1, 0]]

# Explanation: For each intermediate vertex k, check if the path from i to j
#              through k is shorter than the current known path from i to j.
#              dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

def floydWarshall(matrix): #O(V^3)
    V = len(matrix)
    INF = float('inf')

    # Replace -1 with infinity (except diagonal)
    dist = [[0] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif matrix[i][j] == -1:
                dist[i][j] = INF
            else:
                dist[i][j] = matrix[i][j]

    # Floyd-Warshall: try every vertex as intermediate
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Replace infinity back with -1
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                dist[i][j] = -1

    return dist


matrix = [[0, 2, -1, 6],
          [-1, 0, 3, 8],
          [-1, -1, 0, 1],
          [-1, -1, -1, 0]]

result = floydWarshall(matrix)
print("Shortest distance matrix:")
for row in result:
    print(row)
