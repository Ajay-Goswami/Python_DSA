# Problem: Course Schedule I — detect if all courses can be finished (cycle detection in directed graph).
# Input: `numCourses` (int), `prerequisites` (List[List[int]]).
# Output: Returns True if all courses can be finished, otherwise False.
# Time Complexity: O(V + E)

def canFinish(numCourses, prerequisites):
    # Build adjacency list
    adj = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        adj[prereq].append(course)

    visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

    def dfs(node):
        if visited[node] == 1:
            return False   # Cycle detected
        if visited[node] == 2:
            return True    # Already processed

        visited[node] = 1  # Mark as visiting

        for neigh in adj[node]:
            if not dfs(neigh):
                return False

        visited[node] = 2  # Mark as done
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True


numCourses = 2
prerequisites = [[1,0]]

print(canFinish(numCourses, prerequisites))  # True
