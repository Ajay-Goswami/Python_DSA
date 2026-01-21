# Binary Tree Traversals in Binary Tree

from binary_tree import create_sample_tree

tree = create_sample_tree()
root = tree.root

# DFS (Depth First Search) Traversal in Binary Tree - Inorder, Preorder, Postorder (Recursive)
# BFS (Breadth First Search) Traversal in Binary Tree - Levelorder (Iterative)

# DFS Traversals functions
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=' ')

# Print traversals
print("Inorder Traversal:")
inorder_traversal(root)
print("\n")

print("Preorder Traversal:")
preorder_traversal(root)
print("\n")

print("Postorder Traversal:")
postorder_traversal(root)
print("\n")
