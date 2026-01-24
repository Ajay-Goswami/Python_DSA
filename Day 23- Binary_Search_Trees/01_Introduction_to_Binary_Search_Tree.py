# Binary Search Tree (BST) - A binary tree where for each node, all elements in its left subtree are less than the node,
# and all elements in its right subtree are greater than the node. This property allows for efficient searching, insertion, and deletion.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

# Example usage:
if __name__ == "__main__":
    bst = BST()
    root = None
    root = bst.insert(root, 50)
    bst.insert(root, 30)
    bst.insert(root, 20)
    bst.insert(root, 40)
    bst.insert(root, 70)
    bst.insert(root, 60)
    bst.insert(root, 80)

    print("Inorder traversal of the BST:")
    bst.inorder(root)  # Output: 20 30 40 50 60 70 80
