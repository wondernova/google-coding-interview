import math


def test_contiguous_maximum_sum():
    """
    n개의 수들로 이러어진 배열이 있고, 연속된(인접한) 요소들의 합이 최대치인 구간의 합을 구하는 알고리즘을 만드세요
    """
    # Brute Force
    assert 20 == cms_brute_force([-2, 11, -4, 13, -5, 2])
    assert 12 == cms_brute_force([1, 4, -2, -1, 0, 10, -5])
    assert 3 == cms_brute_force([-10, -9, -5, -4, 3, -1])
    assert 3 == cms_brute_force([-10, -9, -5, -4, 3])
    assert 5 == cms_brute_force([5, -10, -9, -5, -4, 3])
    assert 24 == cms_brute_force([5, -10, 5, -3, 22, -10])
    assert 2 == cms_brute_force([0, 0, 1, -1, 1, 1, -1, 1])
    assert -1 == cms_brute_force([-22, -10, -5, -4, -1, -3])
    assert 35 == cms_brute_force([2, 3, 4, 5, 6, 7, 8])

    # Improve Brute Force
    print()
    assert 20 == max_contiguous_sum([-2, 11, -4, 13, -5, 2])
    assert 12 == max_contiguous_sum([1, 4, -2, -1, 0, 10, -5])
    assert 3 == max_contiguous_sum([-10, -9, -5, -4, 3, -1])
    assert 3 == max_contiguous_sum([-10, -9, -5, -4, 3])
    assert 5 == max_contiguous_sum([5, -10, -9, -5, -4, 3])
    assert 24 == max_contiguous_sum([5, -10, 5, -3, 22, -10])
    assert 2 == max_contiguous_sum([0, 0, 1, -1, 1, 1, -1, 1])
    assert -1 == max_contiguous_sum([-22, -10, -5, -4, -1, -3])
    assert 35 == max_contiguous_sum([2, 3, 4, 5, 6, 7, 8])


def cms_brute_force(arr):
    """
    Time Complexity: O(n^3)
    """

    n = len(arr)
    max_sum = -math.inf
    for i in range(n):
        for j in range(i, n):
            _sum = 0
            for l in range(j, n):
                _sum += arr[l]
                if _sum > max_sum:
                    max_sum = _sum
    return max_sum


def max_contiguous_sum(arr):
    """
    Time Complexity: O(n + n) -> O(n)
    Space Complexity: O(1)
    """
    maximum = _cum = 0

    for v in arr:
        if maximum > v:
            maximum = _cum = v

    for i, v in enumerate(arr):
        _cum = max(_cum + v, v)
        if maximum < _cum:
            maximum = _cum
    return maximum
