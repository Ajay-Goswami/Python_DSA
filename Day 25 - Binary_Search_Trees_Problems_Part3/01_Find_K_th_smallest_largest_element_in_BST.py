# Find Kth Smallest/Largest Element in BST - Find the kth smallest or largest element in the BST.

# Input (kthSmallest): root = [3,1,4,null,2], k = 1
# Output (kthSmallest): 1

# Input (kthLargest): root = [3,1,4,null,2], k = 1
# Output (kthLargest): 4

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        return -1

    def kthLargest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.left
        return -1
