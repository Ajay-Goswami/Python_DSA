# Check if a Tree is a BST or Binary Tree - Verify if the given tree is a valid BST or just a binary tree.

# Input (isValidBST): [2,1,3]
# Output (isValidBST): true

# Input (isBinaryTree): [1,2,3]
# Output (isBinaryTree): true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        return helper(root, float('-inf'), float('inf'))

    def isBinaryTree(self, root: Optional[TreeNode]) -> bool:
        return True
