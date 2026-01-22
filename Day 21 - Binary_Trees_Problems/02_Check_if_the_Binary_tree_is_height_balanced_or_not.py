# Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.

# Input: root = [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#      / \
#     15  7
# Output: true

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return dfs(root) != -1