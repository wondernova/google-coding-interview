from tools import create_tree, Node


def test_maximum_width_size():
    node = create_tree([1, 2, None])
    assert 1 == get_width_size(node)

    node = create_tree([1, 2, 3])
    assert 2 == get_width_size(node)

    node = create_tree([1, 2, 3, 4, None, 5, None, 6])
    assert 3 == get_width_size(node)

    node = create_tree([1, 2, 3, None, 4, 5, 6, None, None, 7, None, None, None, None, 8, None, None, None, None, 9])
    assert 6 == get_width_size(node)


def get_width_size(root: Node):
    if root is None:
        return 0

    lefts = {}  # {depth: left position}

    def dfs(node, depth, pos):
        if node is None:
            return 0

        lefts.setdefault(depth, pos)
        max_width = max(dfs(node.left, depth + 1, pos * 2), dfs(node.right, depth + 1, pos * 2 + 1))
        max_width = max(max_width, pos - lefts[depth] + 1)
        return max_width

    max_width = dfs(root, 0, 0)
    return max_width
