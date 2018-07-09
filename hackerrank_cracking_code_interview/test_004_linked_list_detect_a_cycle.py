import random


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def create_random_node():
    N = random.randint(5, 100)
    back_ref = random.randint(0, N - 2)
    back_node = None
    head = curr_node = Node()
    for i in range(N):
        curr_node.data = i

        if i == N - 1:
            curr_node.next = back_node
        else:
            curr_node.next = Node()
            curr_node = curr_node.next

        if back_ref == i:
            back_node = curr_node
    return head


def create_disconneted_node():
    N = random.randint(5, 100)
    head = curr_node = Node()
    for i in range(N):
        curr_node = Node()
        curr_node.data = i
        curr_node.next = Node()
    return head


def test_detect_a_cycle():
    """
    https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
    """
    head = create_random_node()
    assert True == my_answer(head)

    head = create_random_node()
    assert True == my_answer(head)

    head = create_disconneted_node()
    assert False == my_answer(head)

    head = create_disconneted_node()
    assert False == my_answer(head)


def my_answer(head):
    """
    Linked list 안에 cycle이 있는지 조사하는 방법은 2가지 이다.
        1. linked list를 쭉 돌면서 한번 방문한 node는 체크를 한다.
        2. 만약 체크를 할 수 없으면, 속도가 다른 두개의 탐색을 진행시켜서 동일한 node를 꺼내는지 확인한다.
    """
    slow = fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow.next == fast.next.next:
            return True

    return False
