# Top View of Binary Tree

# You are given the root of a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

# Note:
# Return the nodes from the leftmost node to the rightmost node.
# If multiple nodes overlap at the same horizontal position, only the topmost (closest to the root) node is included in the view. 

# Input: root = [1, 2, 3]
# Output: [2, 1, 3]
# Explanation: The Green colored nodes represents the top view in the below Binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List

class Solution:
    def topView(self, root) -> List[int]:
        if not root:
            return []

        hd_map = {}   # horizontal distance -> node value
        queue = deque([(root, 0)])

        while queue:
            node, hd = queue.popleft()

            # store only first node for each horizontal distance
            if hd not in hd_map:
                hd_map[hd] = node.val

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        # return values sorted by horizontal distance
        return [hd_map[k] for k in sorted(hd_map)]
