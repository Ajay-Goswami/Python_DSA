# 03. Cycle Detection in a Directed Graph
# DFS + Recursion Stack

# Problem: Given a directed graph, detect if it contains a cycle.

# Input: V = 4, edges = [[0,1],[1,2],[2,3],[3,1]]
# Output: True
# Explanation: Cycle exists: 1 -> 2 -> 3 -> 1

def isCyclic(V, edges): #O(V + E)
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * V
    recStack = [False] * V

    def dfs(node):
        visited[node] = True
        recStack[node] = True

        for nei in graph[node]:
            if not visited[nei]:
                if dfs(nei):
                    return True
            elif recStack[nei]:
                return True

        recStack[node] = False
        return False

    for i in range(V):
        if not visited[i]:
            if dfs(i):
                return True

    return False

V = 4
edges = [[0,1],[1,2],[2,3],[3,1]]
print(isCyclic(V, edges))
