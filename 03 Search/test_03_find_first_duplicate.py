import math


def test_first_duplicate():
    """
    A = [3, 2, 1, 2, 2, 3] 에서 가장 첫번째 duplicate element는 3 입니다. 2가 아니라.
    """

    assert 3 == find_first_duplicate([3, 2, 1, 2, 2, 3])
    assert 4 == find_first_duplicate([1, 4, 2, 2, 5, 5, 4, 6, 6, 3, 3])
    assert 0 == find_first_duplicate([0, 0, 3, 3, 2, 2])
    assert 0 == find_first_duplicate([0, 3, 3, 2, 2, 0])
    assert -1 == find_first_duplicate([1, 2, 3, 4, 5, 6])


def find_first_duplicate(arr):
    hash = dict()

    for i, v in enumerate(arr):
        if v not in hash:
            hash[v] = i + 1
        elif hash[v] > 0:
            hash[v] *= -1

    smallest_v = -math.inf
    answer = -1
    for k, v in hash.items():
        if smallest_v < v < 0:
            smallest_v = v
            answer = k

    return answer
