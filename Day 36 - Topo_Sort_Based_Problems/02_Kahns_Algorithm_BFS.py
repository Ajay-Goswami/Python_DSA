# 02. Topological Sort using Kahn’s Algorithm
# Graph + BFS + Indegree Concept

# Problem: Given a Directed Acyclic Graph (DAG), return a Topological Ordering using Kahn’s Algorithm (BFS based approach).

# Input: V = 6, edges = [(5, 2),(5, 0),(4, 0),(4, 1),(2, 3),(3, 1)]
# Output: [4, 5, 2, 0, 3, 1]

# Explanation: Nodes with indegree 0 are processed first. Removing their edges may create new indegree-0 nodes.

from collections import deque

def topoSortKahn(V, edges):
    adj = [[] for _ in range(V)]
    indegree = [0] * V

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    topo = []

    while q:
        node = q.popleft()
        topo.append(node)

        for neigh in adj[node]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                q.append(neigh)

    return topo


V = 6
edges = [(5, 2),(5, 0),(4, 0),(4, 1),(2, 3),(3, 1)]

print(topoSortKahn(V, edges))
