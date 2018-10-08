from tools import create_tree


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
