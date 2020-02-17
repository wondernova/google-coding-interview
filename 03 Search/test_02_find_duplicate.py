def test_duplicate_in_integer_array():
    """
    모든 elements 가 0 ~ n-1 사이의 값을 갖고 있다는 조건 하에서
    time complexity O(n) 그리고 space complexity O(1) 으로 문제를 해결할수 있다.
    또한 0은 한번만 나와야 함..
    이런 조건이 아니라면 hash를 쓰는게 가장 빠르다
    """
    arr = [0, 1, 2, 2, 4, 5, 6, 7, 8, 9]
    assert 2 == check_duplicate(arr)

    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8]
    assert 8 == check_duplicate(arr)

    arr = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8]
    assert 1 == check_duplicate(arr)


def check_duplicate(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])] < 0:
            return arr[i]

        arr[arr[i]] = -arr[i]
    return False
