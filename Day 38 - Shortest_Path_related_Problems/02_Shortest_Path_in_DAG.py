# Problem: Shortest Path in DAG — find shortest path from source vertex to all other vertices.

# Input: `n` (number of nodes), `edges` (List[List[int]]), `src` (starting node).
# Output: `dist` list containing shortest distance from source to every other node.
# Time Complexity: O(V + E)

def shortestPath(n, edges, src):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
    
    # Step 1: Perform Topological Sort
    visited = [False] * n
    stack = []
    
    def topoSort(node):
        visited[node] = True
        for v, w in adj[node]:
            if not visited[v]:
                topoSort(v)
        stack.append(node)
    
    for i in range(n):
        if not visited[i]:
            topoSort(i)
            
    # Step 2: Calculate shortest path
    dist = [float('inf')] * n
    dist[src] = 0
    
    while stack:
        node = stack.pop()
        
        if dist[node] != float('inf'):
            for v, w in adj[node]:
                if dist[node] + w < dist[v]:
                    dist[v] = dist[node] + w
                    
    # Replace infinity with -1 for unreachable nodes
    return [d if d != float('inf') else -1 for d in dist]


n = 6
edges = [[0,1,2],[0,4,1],[1,2,3],[2,3,6],[4,2,2],[4,5,4],[5,3,1]]
src = 0

print(shortestPath(n, edges, src))
