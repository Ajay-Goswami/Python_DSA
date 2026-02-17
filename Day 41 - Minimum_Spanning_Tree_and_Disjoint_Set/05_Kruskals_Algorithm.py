# 05. Kruskal's Algorithm - Minimum Spanning Tree
# Graph - Greedy + Disjoint Set Union (Union-Find)

# Problem: Given an undirected, connected, weighted graph with V vertices and E edges,
# find the sum of weights of edges in the Minimum Spanning Tree using Kruskal's Algorithm.
# Kruskal's sorts all edges by weight and greedily picks the smallest edge that
# doesn't form a cycle (checked using Disjoint Set Union).

# Input: V = 5, E = 6, edges = [[0,1,2], [0,2,1], [1,2,1], [2,3,2], [3,4,1], [4,2,2]]
# Output: MST Weight = 5

# Explanation: Sorted edges by weight: (0,2)=1, (1,2)=1, (3,4)=1, (0,1)=2, (2,3)=2, (4,2)=2
#              Pick (0,2)=1 -> no cycle, Pick (1,2)=1 -> no cycle,
#              Pick (3,4)=1 -> no cycle, Pick (0,1)=2 -> forms cycle, skip
#              Pick (2,3)=2 -> no cycle. Total = 1+1+1+2 = 5. MST complete (V-1=4 edges).

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU == rootV:
            return False  # Already in the same set (cycle)

        if self.rank[rootU] < self.rank[rootV]:
            self.parent[rootU] = rootV
        elif self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU
        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1

        return True


def kruskalsAlgorithm(V, edges):  # O(E log E)
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    ds = DisjointSet(V)
    mstWeight = 0
    mstEdges = []

    for u, v, w in edges:
        if ds.union(u, v):
            mstWeight += w
            mstEdges.append((u, v, w))

    return mstWeight, mstEdges


V = 5
E = 6
edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]

mstWeight, mstEdges = kruskalsAlgorithm(V, edges)
print(f"MST Weight (Kruskal's): {mstWeight}")
print(f"MST Edges: {mstEdges}")
