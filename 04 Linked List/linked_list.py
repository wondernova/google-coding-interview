from typing import List, Tuple


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return 'node.{0}'.format(self.value)


def create_linked_list(arr, cycle_idx=None) -> Node:
    root = node = Node(0)
    cycle_node = None

    for i, v in enumerate(arr):
        next_node = Node(v)
        node.next = next_node
        node = next_node
        if cycle_idx == i:
            cycle_node = node

    if cycle_node:
        node.next = cycle_node

    return root.next


def two_linked_list(arr1, arr2, arr3) -> Tuple[Node, Node]:
    root1 = node1 = create_linked_list(arr1)
    while node1.next:
        node1 = node1.next

    root2 = node2 = create_linked_list(arr2)
    while node2.next:
        node2 = node2.next

    join_node = create_linked_list(arr3)
    node1.next = join_node
    node2.next = join_node
    return root1, root2
