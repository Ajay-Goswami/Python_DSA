# 02. Prim's Algorithm - Minimum Spanning Tree
# Graph - Greedy + Priority Queue (Min-Heap)

# Problem: Given an undirected, connected, weighted graph with V vertices and E edges,
# find the sum of weights of edges in the Minimum Spanning Tree using Prim's Algorithm.
# Prim's algorithm grows the MST one vertex at a time by always picking the minimum
# weight edge that connects a visited vertex to an unvisited vertex.

# Input: V = 5, E = 6, edges = [[0,1,2], [0,2,1], [1,2,1], [2,3,2], [3,4,1], [4,2,2]]
# Output: MST Weight = 5

# Explanation: MST edges picked: (0,2)=1, (2,1)=1, (2,3)=2, (3,4)=1
#              Total weight = 1 + 1 + 2 + 1 = 5
#              Prim's starts from node 0, picks minimum weight edges greedily.

import heapq

def primsAlgorithm(V, adj):  # O(E log V)
    visited = [False] * V
    minHeap = [(0, 0)]  # (weight, node)
    mstWeight = 0

    while minHeap:
        weight, node = heapq.heappop(minHeap)

        if visited[node]:
            continue

        visited[node] = True
        mstWeight += weight

        for neighbor, edgeWeight in adj[node]:
            if not visited[neighbor]:
                heapq.heappush(minHeap, (edgeWeight, neighbor))

    return mstWeight


V = 5
E = 6
edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]

adj = [[] for _ in range(V)]
for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))

result = primsAlgorithm(V, adj)
print(f"MST Weight (Prim's): {result}")
