# Problem: Find eventual safe nodes in a directed graph using DFS (cycle detection per node).
# Input: `graph` as adjacency list List[List[int]].
# Output: List[int] of nodes that are eventually safe.
# Time Complexity: O(V + E)

def eventualSafeNodes(graph):

    n = len(graph)
    visited = [0] * n  # 0 = unvisited, 1 = visiting, 2 = safe

    def dfs(node):
        if visited[node] == 1:
            return False
        if visited[node] == 2:
            return True

        visited[node] = 1

        for neigh in graph[node]:
            if not dfs(neigh):
                return False

        visited[node] = 2
        return True

    safe = []
    for i in range(n):
        if dfs(i):
            safe.append(i)

    return safe


graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(eventualSafeNodes(graph))
