from Cython.Compiler.ExprNodes import ListNode


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list_node(nums):
    first = node = ListNode(nums[0])
    for i in nums[1:]:
        node.next = ListNode(i)
        node = node.next
    return first


def get_list(node):
    response = list()
    while node:
        response.append(node.val)
        node = node.next
    return response


def test_add_two_numbers():
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    ```
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
    ```
    """
    l1 = create_list_node([2, 4, 3])
    l2 = create_list_node([5, 6, 4])
    ans = answer(l1, l2)
    ans = get_list(ans)
    assert [7, 0, 8] == ans

    l1 = create_list_node([5])
    l2 = create_list_node([5])
    ans = answer(l1, l2)
    ans = get_list(ans)
    assert [0, 1] == ans


def answer(l1, l2):
    carry = 0
    zero_node = node = ListNode(0)

    while l1 or l2 or carry:
        if l1 is not None:
            carry += l1.val
            l1 = l1.next

        if l2 is not None:
            carry += l2.val
            l2 = l2.next

        node.next = ListNode(carry % 10)
        node = node.next
        carry //= 10

    return zero_node.next
