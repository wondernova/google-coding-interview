def test_find_odds_number():
    """
    정수로 이루어진 배열 A안에 하나의 값을 제외하고 모두 짝수번 나타나고, 값 1개만 홀수번 나타남니다.
    각 요소들의 범위는 1~n 입니다.
    홀수번 나타나는 하나의 값을 찾으세요
    """
    assert 3 == find_odds_number([1, 2, 3, 2, 3, 1, 3])
    assert 5 == find_odds_number([1, 1, 4, 4, 5, 5, 5, 5, 5, 4, 4])


def test_finds_even_number():
    """
    반대로 정수로 이루어진 배열 A안에 하나의 값을 제외하고 1에서 n까지 각 3번 나타납니다.
    각 요소들의 범위는 1~n 입니다.
    값 1개만 양수번 나타납니다.
    양수번 나타나는 값을 찾는 함수를 작성 합니다.
    """
    assert 3 == finds_even_number([1, 3, 1, 5, 1, 2, 3, 4, 2, 4, 2, 4, 6, 5, 6, 7, 6, 7, 7, 5], 7)
    assert 4 == finds_even_number([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5], 5)


def find_odds_number(arr):
    y = 0
    for v in arr:
        y ^= v

    return y


def finds_even_number(arr, n):
    y = 0

    for i, v in enumerate(arr):
        y ^= v

    for i in range(1, n + 1):
        y ^= i

    return y
