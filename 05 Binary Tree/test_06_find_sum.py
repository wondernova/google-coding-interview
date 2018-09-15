from tools import create_tree


def test_find_sum():
    """
    root에서부터 합을 해서 특정 합이 존재하는지 체크하는 함수를 만든다
    """

    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert find_sum(node, 10)

    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert find_sum(node, 1)

    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert find_sum(node, 4)

    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert find_sum(node, 8)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert find_sum(node, 105)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert find_sum(node, 111)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert find_sum(node, 112)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert not find_sum(node, 110)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert not find_sum(node, 113)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert not find_sum(node, 104)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert not find_sum(node, 0)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert find_sum(node, 10)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert find_sum(node, 19)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert find_sum(node, 18)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert find_sum(node, 26)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert find_sum(node, 29)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert find_sum(node, 23)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert not find_sum(node, 24)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert not find_sum(node, 17)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert find_sum(node, 11)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert not find_sum(node, 12)

    node = create_tree([5, 2, 10, None, 9, 6, 22, None, None, None,
                        None, None, None, None, 8, None, None, None, None, None,
                        None, None, None, None, None, None, None, None, None, 9])
    assert find_sum(node, 54)


def find_sum(root, target):
    if not root:
        return False

    remaining = target - root.value
    if remaining == 0:
        return True

    return find_sum(root.left, remaining) or find_sum(root.right, remaining)
