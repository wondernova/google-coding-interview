from linked_list import create_linked_list


def test_palindrome():
    """
    중간에 'x' 가 있는 linked list가 palindrome 인지 아닌지를 판별하는 함수를 만드세요
    """
    node = create_linked_list(['1', 'x', '1'])
    assert check_palindrome(node)

    node = create_linked_list(['a', 'b', 'c', 'x', 'c', 'b', 'a'])
    assert check_palindrome(node)

    node = create_linked_list(['b', 'a', 'a', 'a', 'x', 'a', 'a', 'a', 'b'])
    assert check_palindrome(node)

    node = create_linked_list(['2', 'x', '1'])
    assert not check_palindrome(node)

    node = create_linked_list(['1', 'x', '1', '1'])
    assert not check_palindrome(node)

    node = create_linked_list(['a', 'x', 'b', 'a'])
    assert not check_palindrome(node)

    node = create_linked_list(['a', 'c', 'd', 'x', 'c', 'a'])
    assert not check_palindrome(node)

    node = create_linked_list(['e', 'd', 'a', 'c', 'x', 'c', 'a'])
    assert not check_palindrome(node)


def check_palindrome(root):
    node = root
    stack = []
    while node:
        if node.value == 'x':
            node = node.next
            break

        stack.append(node.value)
        node = node.next

    while node and stack:
        if stack.pop() != node.value:
            break
        node = node.next
    else:
        if not stack and node is None:
            return True
    return False
