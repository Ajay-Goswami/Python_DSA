# GRAPH REPRESENTATION METHODS

# 1. Adjacency List
class Graph:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected graph

# Time Complexity (add edge): O(1)
# Space Complexity: O(V + E)

# 2. Adjacency Matrix
class GraphMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

# Time Complexity (add edge): O(1)
# Space Complexity: O(V^2)

# USAGE

if __name__ == "__main__":
    g1 = GraphMatrix(4)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)

    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    print(g1.matrix)
    print(g2.graph)
