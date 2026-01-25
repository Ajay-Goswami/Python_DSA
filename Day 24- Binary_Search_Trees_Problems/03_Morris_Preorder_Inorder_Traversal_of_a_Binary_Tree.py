# Morris Traversal for Inorder and Preorder - Traverse the binary tree without recursion or stack, using O(1) extra space.

# Input (Inorder): [1,null,2,3]
# Output (Inorder): [1,3,2]

# Input (Preorder): [1,null,2,3]
# Output (Preorder): [1,2,3]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                if not pred.right:
                    pred.right = curr
                    res.append(curr.val)
                    curr = curr.left
                else:
                    pred.right = None
                    curr = curr.right
        return res
