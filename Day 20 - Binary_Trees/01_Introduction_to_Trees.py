# Introduction to Trees

# A tree is a widely used abstract data type that simulates a hierarchical tree structure, with a root value and subtrees of children, represented as a set of linked nodes.

# Basic Terminology:
# 1. Node: A basic unit of a tree that contains data and references to its child nodes.
# 2. Root: The topmost node in a tree.
# 3. Parent: A node that has one or more child nodes.
# 4. Child: A node that is a direct descendant of a parent node.
# 5. Leaf: A node that has no child nodes.
# 6. Sibling: Nodes that share the same parent.
# 7. Subtree: A tree formed by a node and its descendants.
# 8. Depth: The length of the path from the root to a node.
# 9. Height: The length of the longest path from a node to a leaf.
# 10. Ancestor: Any node that is on the path from the root to a given node.
# 11. Descendant: Any node that is a child, grandchild, etc., of a given node.
# 12. Degree: The number of children a node has.
# 13. Level: The set of nodes that are at the same depth in the tree.

# Example of a simple tree structure:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# Creating a simple tree
if __name__ == "__main__":
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(TreeNode(4))
    child1.add_child(TreeNode(5))
    child2.add_child(TreeNode(6))

    # The tree structure is now:
    #        1
    #      /   \
    #     2     3
    #    / \     \
    #   4   5     6


    # Types of Trees:
# 1. Binary Tree: A tree where each node has at most two children.
#         1
#        / \
#       2  3
#      / \
#     4   5

# 2. Binary Search Tree (BST): A binary tree where the left child contains values less than the parent node, and the right child contains values greater than the parent node.
#         4
#        / \
#       2  6
#      / \ / \
#     1  3 5  7


# 3. Balanced Tree: A tree where the height of the two subtrees of any node differ by at most one.
#         1
#        / \
#       2  3
#      / \   \
#     4   5   6

# 4. Complete Tree: A tree where all levels are completely filled except the last level, which is filled from left to right.
#         1
#        / \
#       2  3
#      / \   \
#     4   5   6

# 5. Perfect Tree: A complete binary tree where all internal nodes have two children.
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7

# 6. AVL Tree: A self-balancing binary search tree where the difference in heights between the left and right subtrees cannot be more than one for all nodes.
#         30
#        /  \
#       20   40
#      / \   \
#     10  25  50

# 7. Red-Black Tree: A self-balancing binary search tree where each node is either red or black, and the paths from the root to all leaves form a sequence of black nodes.
#         10 (Black)
#        /  \
#       5 (Red)  15 (Red)
#      / \      / \
#     2  7   12  20

# 8. N-ary Tree: A tree where each node can have at most N children.
#         1
#       / | \
#      2  3  4
#     /|  |
#    5 6  7

# 9. Trie: A tree used to store a dynamic set of strings, where each node represents a common prefix of some strings.
#         root
#        /  \
#       a    b
#      / \    |
#     t   c   a
#    /     \   |
#   e       d  t
#  /         \
# s           e

# 10. Heap: A specialized tree-based data structure that satisfies the heap property (max-heap or min-heap).
#         10
#        /  \
#       9   8
#      / \  / \
#     7  6 5  4
