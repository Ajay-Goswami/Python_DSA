# Bottom View of Binary Tree

#You are given the root of a binary tree, and your task is to return its bottom view. The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.
# Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the latter one in the level order traversal is considered.

# Input: root = [1, 2, 3, 4, 5, N, 6]
# Output: [4, 2, 5, 3, 6]

from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bottomView(self, root) -> List[int]:
        if not root:
            return []

        hd_map = {}   # horizontal distance -> node value
        queue = deque([(root, 0)])

        while queue:
            node, hd = queue.popleft()

            # overwrite value for this horizontal distance
            hd_map[hd] = node.val

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        # return values from leftmost to rightmost
        return [hd_map[k] for k in sorted(hd_map)]
