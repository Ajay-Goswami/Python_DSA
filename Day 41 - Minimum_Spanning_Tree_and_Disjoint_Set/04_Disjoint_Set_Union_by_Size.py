# 04. Disjoint Set Union by Size
# Data Structure - Union-Find with Path Compression and Union by Size

# Problem: Implement a Disjoint Set Union (DSU) data structure using Union by Size.
# Instead of rank, we track the size of each set.
# union(x, y) - Attach the smaller set under the root of the larger set.
# find(x) - Find the representative (root) of the set containing x with path compression.

# Input: n = 7, union(1,2), union(2,3), union(4,5), union(6,7), union(5,6), union(3,7)
# Output: find(3) == find(7) -> True, size of combined set = 7

# Explanation: Union by Size always merges the smaller tree into the larger tree.
#              This keeps the tree balanced and ensures O(α(N)) amortized time.
#              After all unions, all nodes belong to one set of size 7.

class DisjointSet:  # O(α(N)) ≈ O(1) amortized per operation
    def __init__(self, n):
        self.size = [1] * (n + 1)
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

        if self.size[rootU] < self.size[rootV]:
            self.parent[rootU] = rootV
            self.size[rootV] += self.size[rootU]
        else:
            self.parent[rootV] = rootU
            self.size[rootU] += self.size[rootV]


ds = DisjointSet(7)
ds.union(1, 2)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 7)
ds.union(5, 6)
ds.union(3, 7)

print(f"find(3) = {ds.find(3)}, find(7) = {ds.find(7)}")
print(f"3 and 7 in same set: {ds.find(3) == ds.find(7)}")
print(f"Size of set containing 1: {ds.size[ds.find(1)]}")
