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


def test_level_traversal():
    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert [1, 2, 3, 5, 6, 7] == level_traversal(node)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert [100, 5, 6, 7] == level_traversal(node)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] == level_traversal(node)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert [1, 2, 3, 7] == level_traversal(node)

    node = create_tree([])
    assert [] == level_traversal(node)


from collections import deque


def level_traversal(root):
    dq = deque()
    dq.appendleft(root)
    response = []
    i = 0
    while dq:
        node = dq.pop()

        if node is not None:
            response.append(node.value)
            dq.appendleft(node.left)
            dq.appendleft(node.right)

    return response
