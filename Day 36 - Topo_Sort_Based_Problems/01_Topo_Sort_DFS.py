# 01. Topological Sort using DFS
# Graph Traversal Problem (DFS)

# Problem:
# Given a Directed Acyclic Graph (DAG) with V vertices and E edges,
# return a valid Topological Ordering using DFS.

# Input: V = 6, edges = [(5, 2),(5, 0),(4, 0),(4, 1),(2, 3),(3, 1)]
# Output: One valid topological order:
# [5, 4, 2, 3, 1, 0]

# Explanation: In topological sorting, for every directed edge u → v, node u must appear before v in the ordering.

def topoSortDFS(V, edges):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)

    visited = [False] * V
    stack = []

    def dfs(node):
        visited[node] = True
        for neigh in adj[node]:
            if not visited[neigh]:
                dfs(neigh)
        stack.append(node)

    for i in range(V):
        if not visited[i]:
            dfs(i)

    return stack[::-1]


V = 6
edges = [(5, 2),(5, 0),(4, 0),(4, 1),(2, 3),(3, 1)]

print(topoSortDFS(V, edges))
