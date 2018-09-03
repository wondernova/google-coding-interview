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
        self.heap = [math.inf]

    def insert(self, value):
        h = self.heap
        h.append(value)
        cur_idx = len(h) - 1

        while cur_idx > 1:
            if h[cur_idx // 2] > h[cur_idx]:
                h[cur_idx // 2], h[cur_idx] = h[cur_idx], h[cur_idx // 2]
                cur_idx //= 2
            else:
                break
        return cur_idx

    def delete(self, value):
        try:
            cur = self.heap.index(value)
        except ValueError as e:
            print(e)
            return None

        self.heap[cur] = self.heap[-1]
        self.heap = h = self.heap[:len(self.heap) - 1]
        n = len(h)
        while cur * 2 < n:
            child_idx = cur * 2
            if child_idx + 1 < n and h[child_idx + 1] < h[child_idx]:
                child_idx += 1

            if h[child_idx] < h[cur]:
                h[cur], h[child_idx] = h[child_idx], h[cur]
                cur = child_idx
            else:
                break
        return cur

    def peek(self):
        if len(self.heap) <= 1:
            return None

        return self.heap[1]
