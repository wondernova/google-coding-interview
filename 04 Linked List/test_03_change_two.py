from linked_list import to_list, Node, create_linked_list


def test_change_two():
    """
    주어진 연결 리스트가 1 -> 2 -> 3 -> 4 -> None 일때
    2 -> 1 -> 4 -> 3 -> None 으로 바꾸는 함수를 만드세요
    """

    # Recursive Method
    node = create_linked_list([1, 2, 3, 4])
    assert [2, 1, 4, 3] == to_list(use_recursive(node))

    node = create_linked_list([1, 2, 3, 4, 5])
    assert [2, 1, 4, 3, 5] == to_list(use_recursive(node))

    node = create_linked_list([1, 2])
    assert [2, 1] == to_list(use_recursive(node))

    node = create_linked_list([5])
    assert [5] == to_list(use_recursive(node))

    node = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert [2, 1, 4, 3, 6, 5, 8, 7, 9] == to_list(use_recursive(node))

    # Iterative Method
    node = create_linked_list([1, 2, 3, 4])
    assert [2, 1, 4, 3] == to_list(use_iterative(node))

    node = create_linked_list([1, 2, 3, 4, 5])
    assert [2, 1, 4, 3, 5] == to_list(use_iterative(node))

    node = create_linked_list([1, 2])
    assert [2, 1] == to_list(use_iterative(node))

    node = create_linked_list([5])
    assert [5] == to_list(use_iterative(node))

    node = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert [2, 1, 4, 3, 6, 5, 8, 7, 9] == to_list(use_iterative(node))


def use_recursive(node: Node):
    if not node or not node.next:
        return node

    next_node = node.next
    node.next = next_node.next
    next_node.next = node

    node.next = use_recursive(node.next)
    return next_node


def use_iterative(node: Node):
    i = 0
    root = node
    prev_node = None
    while node and node.next:
        next_node = node.next
        node.next = next_node.next
        next_node.next = node

        if i == 0:
            root = next_node

        if prev_node is not None:
            prev_node.next = next_node
        prev_node = node
        node = node.next
        i += 1
    return root
