# 05. Find the City with the Smallest Number of Neighbors in a Threshold Distance
# Graph + Floyd-Warshall Algorithm

# Problem: Given n cities and weighted edges between them, find the city with the
# smallest number of cities that are reachable through some path whose distance
# is at most distanceThreshold. If there are multiple such cities, return the city
# with the greatest number (index).

# Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
# Output: 3

# Explanation: Cities reachable within threshold 4:
#              City 0 -> [1, 2] (2 neighbors)
#              City 1 -> [0, 2, 3] (3 neighbors)
#              City 2 -> [1, 3] (2 neighbors)
#              City 3 -> [1, 2] (2 neighbors)
#              Cities 0, 2, 3 have 2 neighbors each. Return 3 (greatest index).

def findTheCity(n, edges, distanceThreshold): #O(V^3)
    INF = float('inf')

    # Initialize distance matrix
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w

    # Floyd-Warshall: all-pairs shortest path
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Find city with smallest number of reachable neighbors
    min_count = INF
    result_city = -1

    for i in range(n):
        count = 0
        for j in range(n):
            if i != j and dist[i][j] <= distanceThreshold:
                count += 1

        if count <= min_count:
            min_count = count
            result_city = i

    return result_city


n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4

result = findTheCity(n, edges, distanceThreshold)
print(f"City with smallest number of neighbors: {result}")
