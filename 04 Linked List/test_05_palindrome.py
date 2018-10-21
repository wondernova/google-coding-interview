from linked_list import create_linked_list, Node


def test_palindrome():
    """
    A linked list가 주어졌을때 palindrome 인지 아닌지 알아내는 함수를 작성하세요.

    List: 1 -> 2
    Answer: False

    List: 1 -> 2 -> 2 -> 1
    Answer: True

    List: 1 -> 2 -> 1
    Answer: True
    """
    node = create_linked_list([1, 2, 2, 1])
    assert palindrome_with_stack(node) is True

    node = create_linked_list([1, 2, 1])
    assert palindrome_with_stack(node) is True

    node = create_linked_list([3])
    assert palindrome_with_stack(node) is True

    node = create_linked_list([1, 2, 3, 4])
    assert palindrome_with_stack(node) is False

    node = create_linked_list([1, 2, 2, 2])
    assert palindrome_with_stack(node) is False

    node = create_linked_list([1, 2, 3, 2, 2])
    assert palindrome_with_stack(node) is False

    node = create_linked_list([3, 3, 1, 3, 3, 3])
    assert palindrome_with_stack(node) is False

    node = create_linked_list([3, 1, 1, 3, 3])
    assert palindrome_with_stack(node) is False

    node = create_linked_list([5, 6])
    assert palindrome_with_stack(node) is False


def palindrome_with_stack(head: Node):
    slow = fast = head
    stack = list()
    while slow and fast and fast.next:
        stack.append(slow.value)
        fast = fast.next.next
        slow = slow.next

    if fast:
        slow = slow.next

    while stack:
        if stack.pop() != slow.value:
            break
        slow = slow.next
    else:
        return True
    return False
