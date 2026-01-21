# Binary Tree Traversals in Binary Tree

from binary_tree import create_sample_tree

tree = create_sample_tree()
root = tree.root

# BFS (Breadth First Search) Traversal in Binary Tree - Levelorder (Iterative)

# BFS Traversals functions
def levelorder_traversal(root):
    if not root:
        return

    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.value, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


levelorder_traversal(root)
print()
