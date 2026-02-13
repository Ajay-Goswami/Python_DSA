# Problem: Shortest Path in Undirected Graph with Unit Weights — find shortest path from source to all vertices.

# Input: `n` (int), `edges` (List[List[int]]), `src` (int).
# Output: List[int] — shortest distances (-1 if unreachable).
# Time Complexity: O(V + E)

from collections import deque

def shortestPath(n, edges, src):
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Initialize distances
    dist = [-1] * n
    dist[src] = 0
    
    # BFS
    q = deque([src])
    
    while q:
        node = q.popleft()
        
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
                
    return dist


n = 9
edges = [[0,1],[0,3],[1,2],[3,4],[3,7],[4,5],[4,6],[4,7],[5,6],[6,7],[7,8]]
src = 0

print(shortestPath(n, edges, src))
