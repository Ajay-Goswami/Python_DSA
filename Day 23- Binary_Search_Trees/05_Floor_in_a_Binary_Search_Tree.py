# Floor in a Binary Search Tree - The floor of a key is the largest element in the BST that is less than or equal to the key.
# If no such element exists, return -1 or None.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def findFloor(self, root: Optional[TreeNode], key: int) -> Optional[int]:
        floor = None

        while root:
            # Exact match → this itself is the floor
            if root.val == key:
                return root.val

            # If current value is greater, floor must be in left subtree
            if root.val > key:
                root = root.left
            else:
                # Current value can be a floor candidate
                floor = root.val
                root = root.right

        return floor