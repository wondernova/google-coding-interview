from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.child = None
        self.next = None

    def __str__(self):
        return 'n.{0}({1} {2})'.format(self.value,
                                       self.child.value if self.child else None,
                                       self.next.value if self.next else None)

    def __repr__(self):
        return 'n.{0}({1} {2})'.format(self.value, self.child.value if self.child else None, self.next)


def create_tree(arr):
    root = Node(arr[0])
    n = len(arr)

    def f(node, idx):
        is_child = True
        next_node = node
        while idx < n:
            value = arr[idx]
            if value is None:
                return idx + 1

            elif is_child:
                child = Node(value)
                node.child = child
                idx = f(child, idx + 1)
                next_node = child
                is_child = False

            else:
                sibling = Node(value)
                next_node.next = sibling
                next_node = sibling

                idx = f(sibling, idx + 1)

        return idx

    f(root, 1)
    return root


class Node2:
    def __init__(self, value):
        self.value = value
        self._children = list()

    @property
    def children(self) -> List['Node2']:
        return self._children

    def __str__(self):
        return 'n.{0}({1})'.format(self.value, len(self.children))

    def __repr__(self):
        return 'n.{0}({1})'.format(self.value, len(self.children))


def create_tree2(arr):
    root = Node2(arr[0])

    def f(node: Node2, arr: list, i: int = 0):
        if node is None:
            return i + 1

        while i < len(arr):
            value = arr[i]

            if value is None:
                return i + 1
            else:
                child = Node2(value)
                node.children.append(child)
                i = f(child, arr, i + 1)
        return i

    f(root, arr, 1)
    return root
