from tools import create_tree


def test_reversed_traversal():
    """
    level traverse 를 거꾸로 돌린 값을 리턴한다
    :return:
    """
    node = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert [4, 5, 6, 7, 2, 3, 1] == reversed_traversal(node)

    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert [5, 6, 7, 2, 3, 1] == reversed_traversal(node)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert [6, 7, 5, 100] == reversed_traversal(node)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert [3, 2, 1, 0, 7, 6, 5, 4, 9, 8, 10] == reversed_traversal(node)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert [7, 2, 3, 1] == reversed_traversal(node)

    node = create_tree([])
    assert [] == reversed_traversal(node)


from queue import Queue
from collections import deque


def reversed_traversal(root):
    if root is None:
        return []

    queue = Queue()
    queue.put(root)
    response = deque()
    while queue.qsize():
        node = queue.get()
        if node is not None:
            response.appendleft(node.value)
            queue.put(node.right)
            queue.put(node.left)

    return list(response)
