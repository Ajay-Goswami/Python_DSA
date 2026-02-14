# 01. Print the Shortest Path (Dijkstra's Algorithm)
# Graph + BFS + Priority Queue (Min-Heap)

# Problem: Given a weighted undirected graph with V vertices and E edges,
# find the shortest path from source (0) to destination (V-1) and print the path.

# Input: V = 5, edges = [[0,1,2],[1,2,3],[0,3,1],[3,2,1],[2,4,5],[3,4,8]]
# Output: [0, 3, 2, 4] with distance = 7

# Explanation: Use Dijkstra's algorithm with a parent array to track the path.
# After computing shortest distances, backtrack from destination using parent array.

import heapq

def shortestPath(V, edges, src, dest): #O(E log V)
    adj = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    dist = [float('inf')] * V
    parent = list(range(V))
    dist[src] = 0

    pq = [(0, src)]

    while pq:
        d, node = heapq.heappop(pq)

        if d > dist[node]:
            continue

        for v, w in adj[node]:
            if dist[node] + w < dist[v]:
                dist[v] = dist[node] + w
                parent[v] = node
                heapq.heappush(pq, (dist[v], v))

    # If destination is unreachable
    if dist[dest] == float('inf'):
        return -1, []

    # Backtrack to find the path
    path = []
    node = dest
    while node != src:
        path.append(node)
        node = parent[node]
    path.append(src)
    path.reverse()

    return dist[dest], path


V = 5
edges = [[0,1,2],[1,2,3],[0,3,1],[3,2,1],[2,4,5],[3,4,8]]
src = 0
dest = 4

distance, path = shortestPath(V, edges, src, dest)
print(f"Distance: {distance}, Path: {path}")
