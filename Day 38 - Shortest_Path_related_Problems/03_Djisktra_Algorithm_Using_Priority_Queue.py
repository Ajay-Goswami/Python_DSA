# Problem: Dijkstra's Algorithm using Priority Queue — find shortest path in weighted graph.

# Input: `n` (number of nodes), `edges` (List[List[int]]), `src` (starting node).
# Output: `dist` list containing shortest distance from source to all vertices.
# Time Complexity: O(E log V)

import heapq

def dijkstra(n, edges, src):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    pq = [(0, src)]
    dist = [float('inf')] * n
    dist[src] = 0
    
    while pq:
        d, node = heapq.heappop(pq)
        
        if d > dist[node]:
            continue
        
        for v, w in adj[node]:
            if dist[node] + w < dist[v]:
                dist[v] = dist[node] + w
                heapq.heappush(pq, (dist[v], v))
                
    return [d if d != float('inf') else -1 for d in dist]


n = 3
edges = [[0,1,1], [1,2,3], [0,2,6]]
src = 2

# Output: [4, 3, 0]
print(dijkstra(n, edges, src))
