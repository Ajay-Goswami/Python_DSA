# INTRODUCTION TO GRAPHS & TYPES

# A graph is a collection of nodes (vertices) and edges.
# Used to represent networks like roads, social media, internet, etc.

# GRAPH TYPES (NO EXECUTION, ONLY STRUCTURE)

# 1. Undirected Graph: Edge is bidirectional
# 2. Directed Graph (Digraph): Edge has direction
# 3. Weighted Graph: Edges have weights
# 4. Cyclic Graph: Contains cycle
# 5. Acyclic Graph: No cycle
# 6. Connected Graph: Every node reachable
# 7. Disconnected Graph: Multiple components
# 8. DAG: Directed Acyclic Graph (used in scheduling)


# GRAPH REPRESENTATION USING ADJACENCY MATRIX

graph = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

# Time Complexity to access neighbors: O(1)
# Space Complexity: O(V^2)

# GRAPH REPRESENTATION USING ADJACENCY LIST

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

# Time Complexity to access neighbors: O(1)
# Space Complexity: O(V + E)

# GRAPH REPRESENTATION USING Dictionary

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

# Time Complexity to access neighbors: O(1)
# Space Complexity: O(V + E)