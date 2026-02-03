# Brute Force using Adjacency Matrix (DFS)
def dfs_matrix(node, matrix, visited):
    visited[node] = True
    for nei in range(len(matrix)):
        if matrix[node][nei] == 1 and not visited[nei]:
            dfs_matrix(nei, matrix, visited)

def count_components_matrix(matrix):
    n = len(matrix)
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            dfs_matrix(i, matrix, visited)
            count += 1

    return count

# Time Complexity: O(V^2)
# Space Complexity: O(V)


# Optimized using Adjacency List
def dfs_list(node, graph, visited):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs_list(nei, graph, visited)

def count_components_list(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            dfs_list(node, graph, visited)
            count += 1

    return count

# Time Complexity: O(V + E)
# Space Complexity: O(V)

# Run
if __name__ == "__main__":
    matrix = [
        [0,1,0,0],
        [1,0,0,0],
        [0,0,0,1],
        [0,0,1,0]
    ]

    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }

    print(count_components_matrix(matrix))  # 2
    print(count_components_list(graph))     # 2
