from typing import Union

from linked_list import create_linked_list, Node


def test_floyd_algorithm():
    """
    Linked List가 순환루프라면 순환이 일어나는 지점의 Node를 리턴하는 함수를 만들어라.
    만약 순환이 아니라면 None을 리턴한다.
    """
    # Use Hash
    root = create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
    assert 4 == hash_check(root).value

    root = create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert hash_check(root) is None

    root = create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert hash_check(root) is None

    root = create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
    assert 1 == hash_check(root).value

    root = create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
    assert 9 == hash_check(root).value

    # Use Floyd Cycle Finding Algorithm
    root = create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
    assert 4 == floyd(root).value

    root = create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert floyd(root) is None

    root = create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert floyd(root) is None

    root = create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
    assert 1 == floyd(root).value

    root = create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
    assert 9 == floyd(root).value


def hash_check(node) -> Union[Node, None]:
    hash = dict()

    while node:
        idx = id(node)
        if idx in hash:
            return node

        hash.setdefault(idx, 0)
        hash[idx] += 1

        node = node.next
    return None


def floyd(root: Node):
    node1 = node2 = root

    while node1 and node2:
        node1 = node1.next
        node2 = node2.next
        if node2 is None:
            return None
        node2 = node2.next

        if id(node1) == id(node2):
            break

    node1 = root
    while node1 and node2:
        if id(node1) == id(node2):
            return node1
        node1 = node1.next
        node2 = node2.next

    return None
