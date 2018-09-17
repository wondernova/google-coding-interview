def test_find_missing_value():
    """
    배열 A 는 1~ n 로 이루어져 있으며, 중복된 요소는 없습니다.
    이때 빠져있는 정수를 찾는 함수를 만듭니다.

    가장 빠른 방법은 (n*(n+1))/2 를 계산하여 총합을 계산후 빠진 값을 구하는 방법입니다.
    문제는 이 경우 합한 값이 integer의 최대값을 넘으면 정수 오버플로우를 일이킬수 있습니다.
    다른 방법으로 문제를 풀수 있습니까?
    """

    assert 5 == find_missing_value([1, 2, 4, 6, 3, 7, 8], 8)
    assert 2 == find_missing_value([1, 3, 4, 5], 5)


def find_missing_value(arr, n):
    """
    배열안의 모든 값을 xor 로 합한 값을 y 로 정합니다.
    1 에서 n 값까지 모든 값을 xor로 합한 값을 x 로 정합니다.
    x ^ y 의 결과값이 빠진 값입니다.
    """
    y = 0
    for v in arr:
        y ^= v

    x = 0
    for i in range(1, n + 1):
        x ^= i

    return x ^ y
