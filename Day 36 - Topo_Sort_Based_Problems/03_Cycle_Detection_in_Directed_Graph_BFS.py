# 03. Cycle Detection in Directed Graph
# BFS + Kahn’s Algorithm

# Problem: Given a directed graph, check whether it contains a cycle.

# Input: V = 4, edges = [(0, 1),(1, 2),(2, 3),(3, 1)]
# Output: True

# Explanation: If topological sorting does NOT include all nodes, then the graph contains a cycle.

from collections import deque

def detectCycle(V, edges):
    adj = [[] for _ in range(V)]
    indegree = [0] * V

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    count = 0

    while q:
        node = q.popleft()
        count += 1

        for neigh in adj[node]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                q.append(neigh)

    return count != V


V = 4
edges = [(0, 1),(1, 2),(2, 3),(3, 1)]

print(detectCycle(V, edges))
