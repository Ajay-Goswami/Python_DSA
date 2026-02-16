# 02. Number of Ways to Arrive at Destination
# Graph + Dijkstra's Algorithm + Counting Paths

# Problem: Given a weighted undirected graph with n intersections and roads (edges),
# find the number of ways to travel from intersection 0 to intersection n-1
# in the shortest amount of time. Return the count modulo 10^9 + 7.

# Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
# Output: 4

# Explanation: The shortest time to reach node 6 from node 0 is 7.
#              There are 4 different shortest paths: 0->6, 0->1->2->5->6, 0->1->3->5->6, 0->4->6.

import heapq

def countPaths(n, roads): #O(E log V)
    MOD = 10**9 + 7

    adj = [[] for _ in range(n)]
    for u, v, w in roads:
        adj[u].append((v, w))
        adj[v].append((u, w))

    dist = [float('inf')] * n
    ways = [0] * n
    dist[0] = 0
    ways[0] = 1

    pq = [(0, 0)]  # (distance, node)

    while pq:
        d, node = heapq.heappop(pq)

        if d > dist[node]:
            continue

        for v, w in adj[node]:
            new_dist = dist[node] + w

            if new_dist < dist[v]:
                dist[v] = new_dist
                ways[v] = ways[node]
                heapq.heappush(pq, (new_dist, v))
            elif new_dist == dist[v]:
                ways[v] = (ways[v] + ways[node]) % MOD

    return ways[n - 1] % MOD


n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

result = countPaths(n, roads)
print(f"Number of ways: {result}")
