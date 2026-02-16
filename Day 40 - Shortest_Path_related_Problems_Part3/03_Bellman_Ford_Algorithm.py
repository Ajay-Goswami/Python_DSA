# 03. Bellman-Ford Algorithm
# Graph + Dynamic Programming (Relaxation)

# Problem: Given a weighted directed graph with V vertices and E edges,
# find the shortest distances from a source vertex to all other vertices.
# The graph may contain negative weight edges. If a negative weight cycle
# is detected, return [-1].

# Input: V = 5, edges = [[0,1,-1],[0,2,4],[1,2,3],[1,3,2],[1,4,2],[3,2,5],[3,1,1],[4,3,-3]]
#        src = 0
# Output: [0, -1, 2, -2, 1]

# Explanation: Relax all edges V-1 times. If any edge can still be relaxed
#              after V-1 iterations, a negative weight cycle exists.
#              Unlike Dijkstra's, Bellman-Ford handles negative edge weights.

def bellmanFord(V, edges, src): #O(V * E)
    dist = [float('inf')] * V
    dist[src] = 0

    # Relax all edges V-1 times
    for i in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycle (Vth relaxation)
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return [-1]  # Negative cycle detected

    return dist


V = 5
edges = [[0,1,-1],[0,2,4],[1,2,3],[1,3,2],[1,4,2],[3,2,5],[3,1,1],[4,3,-3]]
src = 0

result = bellmanFord(V, edges, src)
print(f"Shortest distances: {result}")
