import math


def test_find_sum_of_two_elements_close_to_zero():
    """
    양수와 음수를 모두 갖는 배열 A에서 두 수의 합이 K에 가까운 요소 2개를 찾으세요.
    A = [1, 60, -10, 70, -80, 85] 이고 K=0 이라면 정답은 -80 그리고 85 입니다.
    """

    # Brute Force
    assert {-80, 85} == close_two_brute_force([1, 60, -10, 70, -80, 85], 0)
    assert {1, 2} == close_two_brute_force([1, 2, 10, 10, 5], 0)
    assert {-1, -2} == close_two_brute_force([-1, -2, -10, -11, -5], 0)
    assert {-4, 4} == close_two_brute_force([0, 10, 5, 4, -4, -3, 1], 0)
    assert {-3100, 3000} == close_two_brute_force([1000, 2000, 3000, -2500, -4000, -3100], 0)
    assert {-10, 60} == close_two_brute_force([1, 60, -10, 70, -80, 85], 45)
    assert {2, 5} == close_two_brute_force([1, 2, 10, 10, 5], 8)
    assert {-11, -5} == close_two_brute_force([-1, -2, -10, -11, -5], -16)

    # With Sort
    assert {-80, 85} == close_two_sorted([1, 60, -10, 70, -80, 85], 0)
    assert {1, 2} == close_two_sorted([1, 2, 10, 10, 5], 0)
    assert {-1, -2} == close_two_sorted([-1, -2, -10, -11, -5], 0)
    assert {-4, 4} == close_two_sorted([0, 10, 5, 4, -4, -3, 1], 0)
    assert {-3100, 3000} == close_two_sorted([1000, 2000, 3000, -2500, -4000, -3100], 0)
    assert {-10, 60} == close_two_sorted([1, 60, -10, 70, -80, 85], 45)
    assert {2, 5} == close_two_sorted([1, 2, 10, 10, 5], 8)
    assert {-11, -5} == close_two_sorted([-1, -2, -10, -11, -5], -16)


def close_two_brute_force(arr, k):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    smallest = math.inf
    answer = None
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            distance = abs(arr[i] + arr[j] - k)
            if distance < smallest:
                smallest = distance
                answer = {arr[i], arr[j]}
    return answer


def close_two_sorted(arr, k):
    arr.sort()

    i, j = 0, len(arr) - 1
    closest = math.inf
    answer = None
    while i < j:
        y = arr[i] + arr[j] - k
        y_abs = abs(y)
        if y_abs < closest:
            closest = y_abs
            answer = {arr[i], arr[j]}

        if y <= 0:
            i += 1
        else:
            j -= 1

    return answer
