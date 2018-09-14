from tools import create_tree


def test_tree_height():
    # With Recursion
    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert 3 == recursive_size(node)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert 3 == recursive_size(node)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert 4 == recursive_size(node)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert 3 == recursive_size(node)

    node = create_tree([1, None, 2, None, None, 3, 4, None, None, None, None, None, None, 5])
    assert 4 == recursive_size(node)

    node = create_tree([])
    assert 0 == recursive_size(node)

    # Without Recursion
    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert 3 == non_recursive_size(node)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert 3 == non_recursive_size(node)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert 4 == non_recursive_size(node)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert 3 == non_recursive_size(node)

    node = create_tree([1, None, 2, None, None, 3, 4, None, None, None, None, None, None, 5])
    assert 4 == non_recursive_size(node)

    node = create_tree([])
    assert 0 == non_recursive_size(node)


from collections import deque


def recursive_size(root):
    if root is None:
        return 0

    return max(recursive_size(root.left),
               recursive_size(root.right)) + 1


def non_recursive_size(root):
    if not root:
        return 0

    dq = deque()
    dq.append(root)
    dq.append(None)

    count = 0
    while dq:
        node = dq.popleft()
        if node is None:
            count += 1
            if len(dq):
                dq.append(None)
        else:
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
    return count
