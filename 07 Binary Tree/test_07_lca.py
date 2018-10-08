from tools import create_tree


def test_least_common_ancestor():
    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert 3 == lca(node, 6, 7)

    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert 1 == lca(node, 2, 7)

    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert 2 == lca(node, 4, 5)

    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert 1 == lca(node, 2, 3)

    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert 1 == lca(node, 5, 7)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert 5 == lca(node, 6, 7)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert 9 == lca(node, 3, 1)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert 9 == lca(node, 3, 0)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert 7 == lca(node, 3, 2)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert 8 == lca(node, 4, 5)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert 10 == lca(node, 2, 5)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert 9 == lca(node, 1, 7)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert 9 == lca(node, 2, 6)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert 9 == lca(node, 7, 0)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert 9 == lca(node, 1, 7)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert 1 == lca(node, 2, 7)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert 1 == lca(node, 7, 2)

    node = create_tree([])
    assert [] == lca(node, 3, 0)


from collections import deque


def lca(root, a, b):
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
