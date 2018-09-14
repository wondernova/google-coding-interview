class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return 'n.{0}'.format(self.value)

    def __repr__(self):
        return 'n.{0}({1} {2})'.format(self.value, self.left, self.right)


def create_tree(arr):
    """
    Accessing Parent Node
        parent_index = (i -1)//2
    """
    if not arr:
        return None

    nodes = [Node(arr[0])]

    i = 1
    while i < len(arr):
        parent_node = nodes[(i - 1) // 2]
        if arr[i] is not None and i % 2 == 0:
            parent_node.right = Node(arr[i])
            nodes.append(parent_node.right)
        elif arr[i] is not None:
            parent_node.left = Node(arr[i])
            nodes.append(parent_node.left)
        else:
            nodes.append(None)
        i += 1

    return nodes[0]


def test_reversed_traversal():
    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert [4, 5, 6, 7, 2, 3, 1] == reversed_traversal(node)

    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert [5, 6, 7, 2, 3, 1] == reversed_traversal(node)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert [6, 7, 5, 100] == reversed_traversal(node)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert [3, 2, 1, 0, 7, 6, 5, 4, 9, 8, 10] == reversed_traversal(node)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert [7, 2, 3, 1] == reversed_traversal(node)

    node = create_tree([])
    assert [] == reversed_traversal(node)


from collections import deque


def reversed_traversal(root):
    if not root:
        return []

    stack = []
    dq = deque()
    dq.appendleft(root)

    while dq:
        node = dq.pop()
        if node is not None:
            stack.append(node.value)
            dq.appendleft(node.right)
            dq.appendleft(node.left)

    return stack[::-1]
