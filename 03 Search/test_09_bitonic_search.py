def test_bitonic_search():
    """
    Bitonic sequence는 값이 계속 증가하다가 중간에 가장 높은 피크를 한번 찍고..
    값이 다시 떨어지는 sequence를 가르킵니다.
    따라서 bitonic sequence의 최소한의 크기는 3입니다.

    예제
    [1, 2, 3, 4, 5, 4, 3, 2, 1]
    [1, 3, 5, 4, 2]

    이때 highest peak를 찍는 index를 리턴시키는 함수를 만듭니다.
    제약사항은 time complexity 는 O(log n)이어야 합니다.


    """

    assert 4 == bitonic_search([1, 2, 3, 4, 5, 4, 3, 2, 1])
    assert 3 == bitonic_search([10, 13, 24, 55, 54])
    assert 1 == bitonic_search([1, 3, 2])
    assert 3 == bitonic_search([-10, -5, -4, 0, -3, -20])
    assert 3 == bitonic_search([-10, -5, -4, -1, -3, -20])
    assert 1 == bitonic_search([-2, -1, -100])
    assert 9 == bitonic_search([1, 3, 5, 7, 9, 11, 13, 17, 19, 23, 1])


def bitonic_search(arr):
    n = len(arr)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        mid_left = max(mid - 1, 0)
        mid_right = min(mid + 1, n - 1)
        if arr[mid_left] < arr[mid] and arr[mid] > arr[mid_right]:
            return mid
        elif arr[mid_left] < arr[mid] < arr[mid_right]:
            left = mid + 1
        else:
            right = mid - 1
    return -1
