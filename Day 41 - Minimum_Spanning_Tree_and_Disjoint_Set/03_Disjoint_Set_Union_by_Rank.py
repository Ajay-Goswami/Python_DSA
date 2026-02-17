# 03. Disjoint Set Union by Rank
# Data Structure - Union-Find with Path Compression and Union by Rank

# Problem: Implement a Disjoint Set Union (DSU) data structure that supports:
# 1. find(x) - Find the representative (root) of the set containing x
# 2. union(x, y) - Merge the sets containing x and y
# Union by Rank attaches the shorter tree under the root of the taller tree.
# Path Compression flattens the tree during find operations.

# Input: n = 7, union(1,2), union(2,3), union(4,5), union(6,7), union(5,6), union(3,7)
# Output: find(3) == find(7) -> True (they belong to the same set after unions)

# Explanation: After all unions, nodes 1-7 are all connected in the same set.
#              Path compression ensures near O(1) amortized time per operation.

class DisjointSet:  # O(α(N)) ≈ O(1) amortized per operation
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])  # Path Compression
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


ds = DisjointSet(7)
ds.union(1, 2)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 7)
ds.union(5, 6)
ds.union(3, 7)

print(f"find(3) = {ds.find(3)}, find(7) = {ds.find(7)}")
print(f"3 and 7 in same set: {ds.find(3) == ds.find(7)}")
print(f"1 and 5 in same set: {ds.find(1) == ds.find(5)}")
