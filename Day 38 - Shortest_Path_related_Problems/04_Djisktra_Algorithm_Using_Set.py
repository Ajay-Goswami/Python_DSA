# Problem: Dijkstra's Algorithm using Set — find shortest path in weighted graph (mimicking C++ set behavior).

# Input: `n` (number of nodes), `edges` (List[List[int]]), `src` (starting node).
# Output: `dist` list containing shortest distance from source to all vertices.
# Time Complexity: O(V * E) with Python set (O(E log V) if using a balanced BST like in C++).

def dijkstra(n, edges, src):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Use a set to store (distance, node)
    # Note: parsing min(q) is O(N) in Python, making this implementation slower than heapq
    # Ideally, a SortedList or similar structure would be used for O(log N) operations
    q = set([(0, src)])
    dist = [float('inf')] * n
    dist[src] = 0
    
    while q:
        # Get element with smallest distance
        d, node = min(q)
        q.remove((d, node))
        
        for v, w in adj[node]:
            if dist[node] + w < dist[v]:
                # If v was already reachable, remove old pair from set
                if dist[v] != float('inf'):
                    if (dist[v], v) in q:
                        q.remove((dist[v], v))
                
                dist[v] = dist[node] + w
                q.add((dist[v], v))
                
    return [d if d != float('inf') else -1 for d in dist]


n = 3
edges = [[0,1,1], [1,2,3], [0,2,6]]
src = 2

# Output: [4, 3, 0]
print(dijkstra(n, edges, src))
