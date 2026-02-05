# Cycle_Detection_in_undirected_Graph_dfs

# Detect cycle in undirected graph using DFS

# Input: V = 5, adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
# Output: True

# Input: V = 3, adj = [[1], [0, 2], [1]]
# Output: False

def is_cycle_dfs(V, adj):  # O(V+E)
    visited = [False] * V

    def dfs(node, parent):
        visited[node] = True
        for nei in adj[node]:
            if not visited[nei]:
                if dfs(nei, node):
                    return True
            elif nei != parent:
                return True
        return False

    for i in range(V):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False


# V = 5
# adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
V = 3
adj = [[1], [0, 2], [1]]

print(is_cycle_dfs(V, adj))