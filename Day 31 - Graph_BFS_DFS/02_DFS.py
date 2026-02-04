# DEPTH FIRST SEARCH (DFS)


def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for nei in graph.get(node, []):
        if nei not in visited:
            dfs(graph, nei, visited)

# Time Complexity: O(V + E)
# Space Complexity: O(V) (recursion stack)

if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0],
        3: [1]
    }

    visited = set()
    dfs(graph, 0, visited)
