# Inorder Successor and Predecessor in BST - Find the inorder successor and predecessor of a given node in the BST.

# Input (inorderSuccessor): root = [2,1,3], p = 1
# Output (inorderSuccessor): 2

# Input (inorderPredecessor): root = [2,1,3], p = 3
# Output (inorderPredecessor): 2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def inorderSuccessor(self, root: Optional[TreeNode], p: Optional[TreeNode]) -> Optional[TreeNode]:
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

    def inorderPredecessor(self, root: Optional[TreeNode], p: Optional[TreeNode]) -> Optional[TreeNode]:
        pred = None
        while root:
            if p.val > root.val:
                pred = root
                root = root.right
            else:
                root = root.left
        return pred
