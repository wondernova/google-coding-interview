from tools import create_tree


def test_delimeter():
    """
    root에서 가장 멀리있는 leaf까지 존재하는 node의 갯수
    """

    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert 3 == delimeter(node)

    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert 3 == delimeter(node)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert 3 == delimeter(node)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert 4 == delimeter(node)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert 3 == delimeter(node)

    node = create_tree([])
    assert 0 == delimeter(node)

    node = create_tree([5, 2, 10, None, 9, 6, 22, None, None, None, None, None, None,
                        None, 8, None, None, None, None, None, None, None, None, None,
                        None, None, None, None, None, 9])
    assert 5 == delimeter(node)


def delimeter(root):
    if not root:
        return 0

    left = delimeter(root.left)
    right = delimeter(root.right)

    return max(left, right) + 1
