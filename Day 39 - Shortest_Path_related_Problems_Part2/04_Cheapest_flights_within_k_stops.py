# 04. Cheapest Flights Within K Stops
# Graph + Modified BFS (Bellman-Ford Variant)

# Problem: Given n cities connected by flights [from, to, price], find the cheapest price
# from src to dst with at most k stops. Return -1 if no such route exists.

# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700

# Explanation: Use a modified Bellman-Ford / BFS approach. Instead of relaxing all edges V-1 times,
# we relax edges only k+1 times (k stops = k+1 edges). We use a queue and process level by level
# to ensure we don't exceed k stops.

from collections import deque

def findCheapestPrice(n, flights, src, dst, k): #O(k * E)
    adj = [[] for _ in range(n)]
    for u, v, w in flights:
        adj[u].append((v, w))

    dist = [float('inf')] * n
    dist[src] = 0

    q = deque([(0, src, 0)])  # (cost, node, stops)

    while q:
        cost, node, stops = q.popleft()

        if stops > k:
            continue

        for v, w in adj[node]:
            if cost + w < dist[v]:
                dist[v] = cost + w
                q.append((cost + w, v, stops + 1))

    return dist[dst] if dist[dst] != float('inf') else -1


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

print(findCheapestPrice(n, flights, src, dst, k))
