from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self._children = list()

    @property
    def children(self) -> List['Node']:
        return self._children

    def __str__(self):
        return 'n.{0}({1})'.format(self.value, len(self.children))

    def __repr__(self):
        return 'n.{0}({1})'.format(self.value, len(self.children))


def create_tree(arr):
    root = Node(arr[0])

    def f(node: Node, arr: list, i: int = 0):
        if node is None:
            return i + 1

        while i < len(arr):
            value = arr[i]

            if value is None:
                return i + 1
            else:
                child = Node(value)
                node.children.append(child)
                i = f(child, arr, i + 1)
        return i

    f(root, arr, 1)
    return root
