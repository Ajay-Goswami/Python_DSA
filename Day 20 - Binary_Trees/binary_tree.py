# Binary Tree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if not current.left:
                current.left = Node(value)
                return
            else:
                queue.append(current.left)

            if not current.right:
                current.right = Node(value)
                return
            else:
                queue.append(current.right)


def create_sample_tree():
    tree = BinaryTree()
    values = [1, 2, 3, 4, 5, 6, 7]
    for v in values:
        tree.insert(v)
    return tree


if __name__ == "__main__":
    tree = create_sample_tree()
