from node_tools import create_tree


def test_preorder():
    root = create_tree([1, 2, 3, None, 4, None, 44, None, 55, None, None, 5, None, 6, 7, 8, 9,
                        None, 10, None, 11, None, 12, None, None, None, None, 20])
    r = preorder(root, [])
    assert [1, 2, 3, 4, 44, 55, 5, 6, 7, 8, 9, 10, 11, 12, 20] == r
    assert 1 == root.value
    assert 2 == root.child.value
    assert 3 == root.child.child.value
    assert 4 == root.child.child.next.value
    assert 44 == root.child.child.next.next.value
    assert 55 == root.child.child.next.next.next.value
    assert 5 == root.child.next.value
    assert 6 == root.child.next.next.value
    assert 7 == root.child.next.next.child.value
    assert 8 == root.child.next.next.child.child.value
    assert 9 == root.child.next.next.child.child.child.value
    assert 10 == root.child.next.next.child.child.child.next.value
    assert 11 == root.child.next.next.child.child.child.next.next.value
    assert 12 == root.child.next.next.child.child.child.next.next.next.value
    assert 20 == root.child.next.next.next.value

    root = create_tree([10, 20, None, 30, None, 40, None, 50, 2, None, None, 60])
    assert [10, 20, 30, 40, 50, 2, 60] == preorder(root, [])


def preorder(node, response=[]):
    if node is None:
        return
    response.append(node.value)
    preorder(node.child, response)
    preorder(node.next, response)
    return response
