def create(data):
    start = node = ListNode(-1)
    for i, val in enumerate(data):
        node.next = ListNode(val)
        node = node.next
    return start.next


def check(expected, node):
    for v in expected:
        assert node is not None
        assert v == node.val
        node = node.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def test_merge_two_sorted_lists():
    a1 = create([1, 2, 4])
    a2 = create([1, 3, 4])
    expected = [1, 1, 2, 3, 4, 4]
    node = merge_two_lists(a1, a2)
    check(expected, node)


def merge_two_lists(l1, l2):
    start = node = ListNode(-1)

    while l1 and l2:
        if l1.val < l2.val:
            node.next = ListNode(l1.val)
            l1 = l1.next
        else:
            node.next = ListNode(l2.val)
            l2 = l2.next
        node = node.next

    while l1:
        node.next = ListNode(l1.val)
        l1 = l1.next
        node = node.next

    while l2:
        node.next = ListNode(l2.val)
        l2 = l2.next
        node = node.next
    return start.next
