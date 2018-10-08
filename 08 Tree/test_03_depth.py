from node_tools import create_tree, Node


def test_general_node_tree_depth():
    node = create_tree([1, 2, 3])
    assert 3 == get_depth(node)

    node = create_tree([1, 2, None, 3, None, 4, None, 5])
    assert 2 == get_depth(node)

    node = create_tree([1, 2, None, 3, 4, None, 5, None, 6, 7, None, 8, 9, 10, 11, 12, None, 13, 14])
    assert 9 == get_depth(node)


def get_depth(node: Node):
    if node is None:
        return 0
    return max(get_depth(node.child) + 1, get_depth(node.next))
