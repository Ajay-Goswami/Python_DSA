# 01. Minimum Spanning Tree
# Graph - Spanning Tree Concept

# Problem: Given an undirected, connected, weighted graph with V vertices and E edges,
# find the sum of weights of the edges in the Minimum Spanning Tree (MST).
# A spanning tree is a tree that connects all vertices with exactly V-1 edges.
# The MST is the spanning tree with the minimum total edge weight.

# Input: V = 3, E = 3, edges = [[0,1,5], [1,2,3], [0,2,1]]
# Output: 4

# Explanation: The MST includes edges (0,2) with weight 1 and (1,2) with weight 3.
#              Total weight = 1 + 3 = 4. This connects all 3 vertices with 2 edges
#              and has the minimum possible total weight.

# Time Complexity: Depends on algorithm used (Prim's or Kruskal's)
# - Prim's: O(E log V) using priority queue
# - Kruskal's: O(E log E) using sorting + union-find

# Note: This file explains the concept. See 02_Prims_Algorithm.py and
#       05_Kruskals_Algorithm.py for actual implementations.

def buildAdjList(V, edges):
    adj = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj


V = 3
E = 3
edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]

adj = buildAdjList(V, edges)
print("Adjacency List representation:")
for i in range(V):
    print(f"  {i} -> {adj[i]}")

print(f"\nTo find MST, use Prim's or Kruskal's algorithm.")
print(f"Expected MST weight: 4 (edges: 0-2 with weight 1, 1-2 with weight 3)")
