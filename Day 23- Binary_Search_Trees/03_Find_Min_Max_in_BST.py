# Find Minimum and Maximum in BST - In a BST, the minimum value is the leftmost node,
# and the maximum value is the rightmost node, due to the BST property.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

class Solution:
    def findMin(self, root: Optional[TreeNode]) -> Optional[int]:
        # If tree is empty
        if root is None:
            return None
        
        # Go to the leftmost node
        while root.left:
            root = root.left
        
        return root.val

    def findMax(self, root: Optional[TreeNode]) -> Optional[int]:
        # If tree is empty
        if root is None:
            return None
        
        # Go to the rightmost node
        while root.right:
            root = root.right
        
        return root.val