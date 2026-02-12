# Problem: Course Schedule II — return a possible course order using topological sort (Kahn's algorithm).
# Input: `numCourses` (int), `prerequisites` (List[List[int]]).
# Output: List[int] representing a valid order of courses, or [] if impossible.
# Time Complexity: O(V + E)

from collections import deque

def findOrder(numCourses, prerequisites):

    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        indegree[course] += 1

    queue = deque()

    # Add nodes with indegree 0
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    topo = []

    while queue:
        node = queue.popleft()
        topo.append(node)

        for neigh in adj[node]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append(neigh)

    if len(topo) == numCourses:
        return topo
    return []


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

print(findOrder(numCourses, prerequisites))
