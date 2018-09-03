import heapq
import math


def test_min_heap():
    # Test 1
    heap = Heap()
    heap.insert(10)
    heap.insert(5)
    assert 5 == heap.peek()
    heap.insert(3)
    assert 3 == heap.peek()
    heap.insert(20)
    assert 3 == heap.peek()
    heap.delete(3)
    assert 5 == heap.peek()
    heap.delete(20)
    assert 5 == heap.peek()
    heap.insert(100)
    heap.insert(-1)
    assert -1 == heap.peek()

    # Test 2
    heap = Heap()
    heap.insert(1)
    heap.insert(1)
    heap.insert(1)
    assert 1 == heap.peek()
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    heap.delete(1)
    assert 1 == heap.peek()
    heap.delete(1)
    assert 1 == heap.peek()
    heap.delete(1)
    assert 2 == heap.peek()
    heap.delete(4)
    assert 2 == heap.peek()
    heap.insert(-20)
    heap.delete(-20)
    assert 2 == heap.peek()
    heap.delete(3)
    assert 2 == heap.peek()
    heap.delete(2)
    assert None == heap.peek()


class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def delete(self, value):
        idx = self.heap.index(value)
        self.heap[idx] = self.heap[-1]
        self.heap = self.heap[:len(self.heap) - 1]
        heapq.heapify(self.heap)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
