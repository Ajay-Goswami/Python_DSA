# 02. Bipartite Graph – BFS / DFS Problem
# Graph Coloring Problem

# Problem: Given a graph, check whether it is bipartite or not. A graph is bipartite if we can color it using two colors such that no two adjacent nodes have the same color.

# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: True
# Explanation: Graph can be colored using two colors without conflict.

from collections import deque

# Using BFS
def isBipartiteBFS(graph): #O(V + E)
    n = len(graph)
    color = [-1] * n

    for start in range(n):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0

            while queue:
                node = queue.popleft()

                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        return False

    return True


graph = [[1,3],[0,2],[1,3],[0,2]]
print(isBipartiteBFS(graph))


# Using DFS

def isBipartiteDFS(graph):  # O(V + E)
    n = len(graph)
    color = [-1] * n

    def dfs(node):
        for nei in graph[node]:
            # If neighbor is not colored, color it with opposite color
            if color[nei] == -1:
                color[nei] = 1 - color[node]
                if not dfs(nei):
                    return False
            # If neighbor has same color → not bipartite
            elif color[nei] == color[node]:
                return False
        return True

    # Handle disconnected graph
    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            if not dfs(start):
                return False

    return True


graph = [[1,3],[0,2],[1,3],[0,2]]
print(isBipartiteDFS(graph))
