import random


def test_searching_in_rotated_array():
    """
    정렬된 배열 A가 어떠한 이유로 한번 회전이 되었습니다.
    해당 배열에서 값을 찾는 알고리즘을 O(log n)으로 만드세요

    A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14] 에서 5를 찾으세요
    결과 8 (index)

    한번에 해결할수 있는 코드는 09번 bitonic search를 사용하면 됨
    """

    # Test find_pivot
    for _ in range(20):
        n = random.randint(3, 20)
        pivot_true = random.randint(1, n - 1)
        arr = list(range(n))
        arr = arr[pivot_true:] + arr[:pivot_true]
        pivot_pred = find_pivot(arr, 0, len(arr) - 1)
        assert n - pivot_true == pivot_pred

    # Pivot
    assert 8 == search_pivot([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5)
    assert 0 == search_pivot([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 15)
    assert 5 == search_pivot([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 1)
    assert 4 == search_pivot([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 25)
    assert 11 == search_pivot([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 14)
    assert 0 == search_pivot([15, 10, 13, 14], 15)
    assert 1 == search_pivot([15, 10, 13, 14], 10)
    assert 3 == search_pivot([15, 10, 13, 14], 14)


def search_pivot(arr, target):
    pivot = find_pivot(arr, 0, len(arr) - 1)

    if target >= arr[0]:
        return binary_search(arr, 0, pivot, target)
    else:
        return binary_search(arr, pivot, len(arr) - 1, target)


def find_pivot(arr, start, end):
    if start == end:
        return end
    elif start == end - 1:
        if arr[start] >= arr[end]:
            return end
        else:
            return start

    mid = (start + end) // 2
    if arr[start] <= arr[mid]:
        return find_pivot(arr, mid, end)
    else:
        return find_pivot(arr, start, mid)


def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
