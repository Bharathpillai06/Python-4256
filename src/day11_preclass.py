class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)


def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))


if __name__ == "__main__":
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    print("Postorder traversal:")
    postorder(root)

    print("Height:", height(root))
