from linked_list import two_linked_list, Node


def test_joined_two_linked_list():
    """
    두개의 linked list는 서로 시작점은 다르지만 중간 어디에서 서로 합류를 하게 됩니다.
    예를 들어서 다음과 같습니다.

    A -> B -> C ->
                    D -> E -> F
         H -> I ->

    중간에 서로 합류하는 node를 찾으세요
    이때 합류하는 지점까지의 두 linked list의 길이는 서로 다릅니다.
    """
    # Use Hash
    root1, root2 = two_linked_list([1, 2, 3, 4], [20, 30], [100, 200, 300])
    assert 100 == use_hash(root1, root2).value

    root1, root2 = two_linked_list([1], [20, 30, 40, 50, 60, 70, 80], [200, 400, 500])
    assert 200 == use_hash(root1, root2).value

    root1, root2 = two_linked_list([1, 2, 3, 4, 5, 6], [20], [300, 400, 500])
    assert 300 == use_hash(root1, root2).value

    root1, root2 = two_linked_list([1, 2, 3], [20, 30, 40], [400, 500, 600])
    assert 400 == use_hash(root1, root2).value

    # Use Stack
    root1, root2 = two_linked_list([1, 2, 3, 4], [20, 30], [100, 200, 300])
    assert 100 == use_stack(root1, root2).value

    root1, root2 = two_linked_list([1], [20, 30, 40, 50, 60, 70, 80], [200, 400, 500])
    assert 200 == use_stack(root1, root2).value

    root1, root2 = two_linked_list([1, 2, 3, 4, 5, 6], [20], [300, 400, 500])
    assert 300 == use_stack(root1, root2).value

    root1, root2 = two_linked_list([1, 2, 3], [20, 30, 40], [400, 500, 600])
    assert 400 == use_stack(root1, root2).value


def use_hash(node1: Node, node2: Node):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    hash = dict()

    while node1 or node2:

        if node1:
            idx = id(node1)
            if idx in hash:
                return node1
            hash[idx] = 0
            node1 = node1.next

        if node2:
            idx = id(node2)
            if idx in hash:
                return node2
            hash[idx] = 0
            node2 = node2.next

    return None


def use_stack(node1: Node, node2: Node):
    """
    Time Complexity: O(n + m) 두 리스트를 탐색하는 시간
    Space Complexity: O(n + m)
    """
    stack1, stack2 = list(), list()

    node = node1
    while node:
        stack1.append(node)
        node = node.next

    node = node2
    while node:
        stack2.append(node)
        node = node.next

    joined_node = None
    while stack1 and stack2:
        node1 = stack1.pop()
        node2 = stack2.pop()

        if id(node1) == id(node2):
            joined_node = node1
        else:
            break
    return joined_node
