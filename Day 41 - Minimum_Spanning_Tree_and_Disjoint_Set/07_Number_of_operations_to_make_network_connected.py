# 07. Number of Operations to Make Network Connected
# Graph - Disjoint Set Union (Union-Find)

# Problem: Given n computers numbered from 0 to n-1 and a list of connections where
# connections[i] = [a, b] means computer a and b are connected. You can remove a cable
# between two directly connected computers and place it between any pair of disconnected
# computers to make them directly connected. Return the minimum number of operations
# needed to connect all computers. If it's not possible, return -1.

# Input: n = 6, connections = [[0,1], [0,2], [0,3], [1,2], [1,3]]
# Output: 2

# Explanation: We need at least n-1 = 5 cables to connect 6 computers. We have 5 cables.
#              Extra cables (forming cycles): (1,2) and (1,3) are redundant.
#              Components: {0,1,2,3}, {4}, {5} -> 3 components.
#              We need 3-1 = 2 operations to connect all components.
#              If total cables < n-1, return -1 (not enough cables).

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU == rootV:
            return False  # Already connected (extra cable)

        if self.rank[rootU] < self.rank[rootV]:
            self.parent[rootU] = rootV
        elif self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU
        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1

        return True


def makeConnected(n, connections):  # O(E * α(N))
    if len(connections) < n - 1:
        return -1  # Not enough cables

    ds = DisjointSet(n)
    extraCables = 0

    for u, v in connections:
        if not ds.union(u, v):
            extraCables += 1

    # Count number of connected components
    components = len(set(ds.find(i) for i in range(n)))

    # Need (components - 1) cables to connect all components
    return components - 1


n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
result = makeConnected(n, connections)
print(f"Minimum operations to connect network: {result}")
