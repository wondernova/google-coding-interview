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
    assert [1, 2, 5, 3, 6, 7] == preorder(node)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert [100, 5, 6, 7] == preorder(node)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert [10, 9, 7, 3, 2, 6, 1, 0, 8, 5, 4] == preorder(node)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert [1, 2, 3, 7] == preorder(node)

    node = create_tree([])
    assert [] == preorder(node)


def preorder(root):
    if not root:
        return []

    stack = list()
    stack.append(root)

    response = []
    while stack:
        node = stack.pop()
        if node:
            response.append(node.value)
            stack.append(node.right)
            stack.append(node.left)
    return response
