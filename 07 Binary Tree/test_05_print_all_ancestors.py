from tools import create_tree


def test_print_all_ancestors():
    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert [1] == get_ancestors(node, 1)

    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert [1, 3] == get_ancestors(node, 3)

    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert [1, 2] == get_ancestors(node, 2)

    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert [1, 3, 6] == get_ancestors(node, 6)

    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert [1, 3, 7] == get_ancestors(node, 7)

    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert [1, 2, 4] == get_ancestors(node, 4)

    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert [1, 2, 5] == get_ancestors(node, 5)

    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert [1, 2, 5] == get_ancestors(node, 5)

    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert None == get_ancestors(node, 17)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert [100, 5] == get_ancestors(node, 5)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert [100, 5, 7] == get_ancestors(node, 7)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert None == get_ancestors(node, 0)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert [10, 9, 6, 0] == get_ancestors(node, 0)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert [10, 9, 6, 1] == get_ancestors(node, 1)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert [10, 9, 7, 2] == get_ancestors(node, 2)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert [10, 9, 7, 3] == get_ancestors(node, 3)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert [10, 8, 4] == get_ancestors(node, 4)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert [10, 8, 5] == get_ancestors(node, 5)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert None == get_ancestors(node, -1)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert None == get_ancestors(node, 11)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert [1, 3, 7] == get_ancestors(node, 7)

    node = create_tree([5, 2, 10, None, 17, 6, 22, None, None, None,
                        None, None, None, None, 8, None, None, None, None, None,
                        None, None, None, None, None, None, None, None, None, 9])
    assert [5, 10, 22, 8, 9] == get_ancestors(node, 9)

    node = create_tree([5, 2, 10, None, 17, 6, 22, None, None, None,
                        None, None, None, None, 8, None, None, None, None, None,
                        None, None, None, None, None, None, None, None, None, 9])
    assert None == get_ancestors(node, 15)

    node = create_tree([])
    assert None == get_ancestors(node, 0)


def get_ancestors(root, target):
    if not root:
        return None

    if root.value == target:
        l = [root.value]
        return l

    left = get_ancestors(root.left, target)
    right = get_ancestors(root.right, target)

    l = left or right
    if l:
        l.insert(0, root.value)

    return l


from collections import deque


def get_ancestors2(root, target):
    ancestors = deque()

    def f(root):
        if not root:
            return []

        if root.value == target or f(root.left) or f(root.right):
            ancestors.appendleft(root.value)
            return ancestors
        return []

    return list(f(root))
