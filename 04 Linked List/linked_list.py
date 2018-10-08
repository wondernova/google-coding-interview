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
