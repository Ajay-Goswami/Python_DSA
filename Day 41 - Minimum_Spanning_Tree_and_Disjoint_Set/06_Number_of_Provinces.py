# 06. Number of Provinces
# Graph - Disjoint Set Union (Union-Find)

# Problem: Given an adjacency matrix where isConnected[i][j] = 1 means city i and city j
# are directly connected, find the total number of provinces. A province is a group of
# directly or indirectly connected cities with no other cities outside the group.

# Input: isConnected = [[1,1,0], [1,1,0], [0,0,1]]
# Output: 2

# Explanation: Cities 0 and 1 are connected (province 1). City 2 is alone (province 2).
#              Using DSU: union(0,1) -> {0,1} and {2} -> 2 distinct sets = 2 provinces.

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
            return

        if self.rank[rootU] < self.rank[rootV]:
            self.parent[rootU] = rootV
        elif self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU
        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1


def findNumberOfProvinces(isConnected):  # O(V^2 * α(V))
    V = len(isConnected)
    ds = DisjointSet(V)

    for i in range(V):
        for j in range(i + 1, V):
            if isConnected[i][j] == 1:
                ds.union(i, j)

    # Count distinct roots
    provinces = len(set(ds.find(i) for i in range(V)))
    return provinces


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
result = findNumberOfProvinces(isConnected)
print(f"Number of Provinces: {result}")
