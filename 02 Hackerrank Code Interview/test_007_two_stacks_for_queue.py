def test_use_two_stacks_to_implement_deque():
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
    Instack : LIFO (last in first out)
    Outstack : FIFO (first in first out)

    이렇게 두개의 stacks을 만들되.. 서로 들오고 나가는 순서가 다른 stacks으로 구현을 하는게 포인트이다.
    또한 매번 instack -> outstack으로 전환하는 과정의 연산을 줄이기 위해서 필요할때만 하도록 만드는것이 포인트이다.
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
