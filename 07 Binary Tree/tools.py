class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return 'n.{0}'.format(self.value)

    def __repr__(self):
        return 'n.{0}({1} {2})'.format(self.value, self.left, self.right)


def create_tree(arr):
    """
    Accessing Parent Node
        parent_index = (i -1)//2
    """
    if not arr:
        return None

    nodes = [Node(arr[0])]

    i = 1
    while i < len(arr):
        parent_node = nodes[(i - 1) // 2]
        if arr[i] is not None and i % 2 == 0:
            parent_node.right = Node(arr[i])
            nodes.append(parent_node.right)
        elif arr[i] is not None:
            parent_node.left = Node(arr[i])
            nodes.append(parent_node.left)
        else:
            nodes.append(None)
        i += 1

    return nodes[0]
