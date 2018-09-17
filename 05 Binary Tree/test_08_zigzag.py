from tools import create_tree


def test_level_traversal():
    """
    각 레벨마다 지그재그로 travasal하는 함수를 만든다.
    최초 root에서 왼쪽에서 우측으로 읽고 (어차피 루트하나)..
    그 다음 레벨에서 우측에서 왼쪽으로 읽고..
    그 다음 레벨에서 좌측에서 우측으로 읽고.. 반복..
    """
    node = create_tree([1, 2, 3, None, 5, 6, 7])
    assert [1, 3, 2, 5, 6, 7] == zigzag(node)

    node = create_tree([100, None, 5, None, None, 6, 7])
    assert [100, 5, 6, 7] == zigzag(node)

    node = create_tree([100, 4, 5, 3, None, 6, 7])
    assert [100, 5, 4, 3, 6, 7] == zigzag(node)

    node = create_tree([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert [10, 8, 9, 7, 6, 5, 4, 0, 1, 2, 3] == zigzag(node)

    node = create_tree([1, 2, 3, None, None, None, 7])
    assert [1, 3, 2, 7] == zigzag(node)

    node = create_tree([])
    assert [] == zigzag(node)


from collections import deque


def zigzag(root):
    flag = 0  # 0: left to right, 1: right to left on stack
    stack, response = list(), list()
    dq = deque()
    dq.appendleft(root)

    while dq:
        node = dq.pop()

        if node:
            response.append(node.value)

        if node and flag == 0:
            stack.append(node.left)
            stack.append(node.right)
        elif node:
            stack.append(node.right)
            stack.append(node.left)

        if not dq:
            for _ in range(len(stack)):
                dq.appendleft(stack.pop())

            flag = 1 - flag

    return response
