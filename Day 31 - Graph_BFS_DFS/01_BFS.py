# BREADTH FIRST SEARCH (BFS)

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for nei in graph.get(node, []):
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)

# Time Complexity: O(V + E)
# Space Complexity: O(V)

# EDGE CASES HANDLED
# - Empty graph
# - Single node

if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0],
        3: [1]
    }

    bfs(graph, 0)
