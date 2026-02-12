# Problem: Given a sorted dictionary (words) of an alien language, derive the character order.
# Input: `words` as List[str].
# Output: A string representing a valid character ordering, or empty string if not possible.
# Time Complexity: O(V + E) where V is number of unique characters and E is number of precedence edges.

from collections import deque

def alienOrder(words):

    adj = {}
    indegree = {}

    # Initialize
    for word in words:
        for char in word:
            adj[char] = []
            indegree[char] = 0

    # Build graph
    for i in range(len(words)-1):
        w1 = words[i]
        w2 = words[i+1]
        minLen = min(len(w1), len(w2))

        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].append(w2[j])
                indegree[w2[j]] += 1
                break

    # Kahn’s Algorithm
    queue = deque()

    for char in indegree:
        if indegree[char] == 0:
            queue.append(char)

    topo = ""

    while queue:
        char = queue.popleft()
        topo += char

        for neigh in adj[char]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append(neigh)

    if len(topo) == len(indegree):
        return topo
    return ""


words = ["baa","abcd","abca","cab","cad"]
print(alienOrder(words))
