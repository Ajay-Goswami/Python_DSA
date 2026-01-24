# Search in a Binary Search Tree - Searching in a BST is efficient due to its ordered property.
# We start from the root and move left if the key is smaller, right if larger, until we find the key or reach a null node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case: empty tree or value found
        if root is None or root.val == val:
            return root
        
        # If value is smaller, search left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If value is greater, search right subtree
        return self.searchBST(root.right, val)
