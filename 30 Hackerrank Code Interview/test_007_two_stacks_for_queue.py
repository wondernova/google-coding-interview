def test_use_two_stacks_to_implement_deque():
    """
    https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem

    2개의 stacks을 사용해서 queue를 만들어라.

    참고. Stack 과 Queue의 차이
    Stack is a LIFO (last in first out) data structure.
    Queue is a FIFO (first in first out) data structure.

    """

    # First Test
    queue = MyQueue()
    queue.put(42)  # [42]
    assert 42 == queue.pop()  # []
    queue.put(14)  # [14]
    assert 14 == queue.peek()
    queue.put(28)  # [14, 28]
    assert 14 == queue.peek()
    queue.put(60)  # [14, 28, 60]
    queue.put(78)  # [14, 28, 60, 78]
    assert 14 == queue.peek()
    assert 14 == queue.pop()  # [28, 60, 78]
    assert 28 == queue.pop()  # [60, 78]
    assert 60 == queue.pop()  # [78]
    queue.put(44)  # [78, 44]
    assert 78 == queue.peek()
    assert 78 == queue.pop()  # [44]
    assert 44 == queue.pop()


class MyQueue(object):
    """

    """

    def __init__(self):
        self.instack = list()
        self.outstack = list()

    def put(self, element):
        self.instack.append(element)

    def peek(self):
        self.shift()
        peek = self.outstack[-1]
        return peek

    def pop(self):
        self.shift()
        value = self.outstack.pop()
        return value

    def shift(self):
        """
        Move elements from instack to outstack
        """
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
