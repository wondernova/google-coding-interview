from tools import create_tree


def test_non_recursive_traversal():
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
