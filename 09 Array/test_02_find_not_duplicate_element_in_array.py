def test_finding_not_duplicate_element_in_array():
    """
    주어지는 array의 모든 elements는 모두 2개씩 중복으로 존재한다.
    하지만 단 하나의 element만 중복없이 한번만 존재한다.
    중복하지 않는 해당 element값이 무엇인지 리턴하여라
    """
    assert 1 == find_not_duplicate_index([2, 3, 2, 3, 1, 4, 4])
    assert 2 == find_not_duplicate_index([3, 4, 5, 3, 4, 2, 5])
    assert 0 == find_not_duplicate_index([-1, -1, 0, 2, 2, 3, 3])
    assert -3 == find_not_duplicate_index([-3, 0, 1, 4, 0, 4, 1])


def find_not_duplicate_index(arr):
    r = 0
    for v in arr:
        r ^= v
    return r
