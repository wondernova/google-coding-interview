import random

import numpy as np
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def put_value(root, value):
    if root.left is not None and root.data > value:
        return put_value(root.left, value)
    elif root.right is not None and root.data <= value:
        return put_value(root.right, value)
    elif root.left is None and root.data > value:
        root.left = Node(value)
        return True
    elif root.right is None and root.data <= value:
        root.right = Node(value)
        return True


def create_valid_binary_search_tree():
    data = random.sample(range(0, 200), 20)
    root = Node(data[0])

    for value in data[1:]:
        put_value(root, value)

    return root


def test_detect_a_cycle():
    """
    https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem

    Binary Search tree는 root node를 기준으로 왼쪽으로는 root node보다 작은 값이 그리고 오른쪽으로는 더 큰 값이 와야 합니다.
    하지만 이때 sub tree에서 예를 들어서 부모 노드의 값보다 더 큰 값이 오른쪽에 있거나.. 하여튼 그러면 안됨.
    Binary search tree를 자세하게 알려면 링크 열고 확인.

    문제는 binary search tree인지 아닌지 알아내는 함수 짤것

    조건으로 모든 값은 unique하다
    """
    root = create_valid_binary_search_tree()
    answer = my_answer(root)
    assert answer


def my_answer(root):
    """
    Binary search tree는 left 그리고 right 두가지 방향을 갖은 트리이다.
    이때 현재 노드의 값보다 left는 더 작아야 하고, 오른쪽은 더 커야 한다.
    함수는 binary search tree인지 아닌지 판단하다.
    """

    return check_binary_search_tree(root, float('-inf'), float('inf'))


def check_binary_search_tree(root, minimum, maximum):
    # 만약 노드의 끝에 도착했다면, True를 리턴시킨다.
    if root is None:
        return True

    # minimum 보다 작으면 안되고, maximum 보다 크면 안된다
    if root.data < minimum or root.data > maximum:
        return False

    return (check_binary_search_tree(root.left, minimum, root.data - 1) and
            check_binary_search_tree(root.right, root.data + 1, maximum))
