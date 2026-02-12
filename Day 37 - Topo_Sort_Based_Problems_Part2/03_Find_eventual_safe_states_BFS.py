# Problem: Find eventual safe nodes in a directed graph using BFS (reverse graph + Kahn's algorithm).
# Input: `graph` as adjacency list List[List[int]].
# Output: Sorted List[int] of nodes that are eventually safe.
# Time Complexity: O(V + E)

from collections import deque

def eventualSafeNodes(graph):

    n = len(graph)
    reverse_adj = [[] for _ in range(n)]
    indegree = [0] * n

    for u in range(n):
        for v in graph[u]:
            reverse_adj[v].append(u)
            indegree[u] += 1

    queue = deque()

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    safe = []

    while queue:
        node = queue.popleft()
        safe.append(node)

        for neigh in reverse_adj[node]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append(neigh)

    return sorted(safe)


# Example
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(eventualSafeNodes(graph))
