from node_tools import create_tree2, Node2


def test_preorder():
    root = create_tree2([1, 2, 3, None, 4, None, None, 5, None, 6, 7, 8, 9, None, 10, None, 11])
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] == preorder(root, [])

    root = create_tree2([1, 2, 3, 4, None, 5, 6, 7, None, None, 8, None, 9, 10, None, None, None, None, None, 20])
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20] == preorder(root, [])
    assert 1 == root.value
    assert 2 == root.children[0].value
    assert 20 == root.children[1].value
    assert 3 == root.children[0].children[0].value
    assert 4 == root.children[0].children[0].children[0].value
    assert 5 == root.children[0].children[0].children[1].value

    root = create_tree2([10, 9, None, 8, None, 7, 6, None, 5, None, 4, None, 3])
    assert [10, 9, 8, 7, 6, 5, 4, 3] == preorder(root, [])

    root = create_tree2([10, 9, None, 8, None, 7, 6, None, 5, None, 4, None, 3])
    assert [10, 9, 8, 7, 6, 5, 4, 3] == preorder(root, [])


def preorder(node: Node2, response: list):
    response.append(node.value)
    for child_node in node.children:
        preorder(child_node, response)

    return response
