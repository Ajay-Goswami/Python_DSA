# Cycle_Detection_in_undirected_Graph_bfs

# Detect cycle in undirected graph using BFS

# Input: V = 5, adj = [[1],[0,2,4],[1,3],[2,4],[1,3]]
# Output: True


from collections import deque

def is_cycle_bfs(V, adj):  # O(V+E)
    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            queue = deque([(i, -1)])
            visited[i] = True

            while queue:
                node, parent = queue.popleft()
                for nei in adj[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append((nei, node))
                    elif nei != parent:
                        return True
    return False


V = 5
adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]

print(is_cycle_bfs(V, adj))