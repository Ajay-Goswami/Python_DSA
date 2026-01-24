# Ceil in a Binary Search Tree - The ceil of a key is the smallest element in the BST that is greater than or equal to the key.
# If no such element exists, return -1 or None.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def findCeil(self, root: Optional[TreeNode], key: int) -> Optional[int]:
        ceil = None

        while root:
            # If exact match, this is the ceil
            if root.val == key:
                return root.val

            # If current value is smaller, ceil must be in right subtree
            if root.val < key:
                root = root.right
            else:
                # Current value can be a ceil candidate
                ceil = root.val
                root = root.left

        return ceil