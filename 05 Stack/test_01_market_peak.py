def test_market_peak():
    """
    Span 문제로서 예를 들어서 주식시장에서 "52주 최고치" 이런말이 있습니다.
    주식시장에서 어느기간동안의 peak를 찍었는지를 알아내는 알고리즘을 만듭니다.

    예를 들어서
    [6, 3, 4, 5, 2] 에 대한 span값은 다음과 같습니디.
    [1, 1, 2, 3, 1]

    입력값은 양수를 갖은 array입니다.
    """

    # Brute Force
    assert [1, 1, 2, 3, 1] == span_brute_force([6, 3, 4, 5, 2])
    assert [1, 1, 1, 2, 4] == span_brute_force([4, 2, 1, 2, 3])
    assert [1, 2, 3, 4, 5] == span_brute_force([2, 5, 6, 7, 8])
    assert [1, 1, 1, 1] == span_brute_force([10, 9, 4, 1])
    assert [1, 1, 1] == span_brute_force([5, 5, 5])
    assert [1, 1, 3, 1, 2, 3, 7, 1, 9] == span_brute_force([5, 2, 10, 4, 6, 7, 20, 1, 30])
    assert [] == span_brute_force([])

    # Using Stack
    assert [1, 1, 2, 3, 1] == span_with_stack([6, 3, 4, 5, 2])
    assert [1, 1, 1, 2, 4] == span_with_stack([4, 2, 1, 2, 3])
    assert [1, 2, 3, 4, 5] == span_with_stack([2, 5, 6, 7, 8])
    assert [1, 1, 1, 1] == span_with_stack([10, 9, 4, 1])
    assert [1, 1, 1] == span_with_stack([5, 5, 5])
    assert [1, 1, 3, 1, 2, 3, 7, 1, 9] == span_with_stack([5, 2, 10, 4, 6, 7, 20, 1, 30])
    assert [] == span_with_stack([])


def span_brute_force(arr):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """

    span = list()
    for i in range(len(arr)):
        j = 1
        while j <= i and arr[i] > arr[i - j]:
            j += 1
        span.append(j)
    return span


def span_with_stack(arr):
    stack = list()
    span = list()

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()

        if not stack:
            p = -1
        else:
            p = stack[-1]

        span.append(i - p)
        stack.append(i)
    return span
