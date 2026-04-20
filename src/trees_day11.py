class Node:
    def __init__(self, value, left_child=None, right_child=None):
        self.val = value
        self.left = left_child
        self.right = right_child

    def __str__(self):
        return str(self.val)

def num_nodes(root):
    if root is None:
        return 0
    return 1 + num_nodes(root.left) + num_nodes(root.right)


def num_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return num_leaves(root.left) + num_leaves(root.right)


def is_full(root):
    if root is None:
        return True
    if (root.left is None) != (root.right is None):
        return False
    return is_full(root.left) and is_full(root.right)


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def is_perfect(root):
    return num_nodes(root) == 2 ** height(root) - 1


def has_value_bst(root, val):
    if root is None:
        return False
    if val == root.val:
        return True
    if val < root.val:
        return has_value_bst(root.left, val)
    return has_value_bst(root.right, val)


def add_value_bst(bst, value):
    if value < bst.val:
        if bst.left is None:
            bst.left = Node(value)
        else:
            add_value_bst(bst.left, value)
    else:
        if bst.right is None:
            bst.right = Node(value)
        else:
            add_value_bst(bst.right, value)


def add(heap, val):
    heap.append(val)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break