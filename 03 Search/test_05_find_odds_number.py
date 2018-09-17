def test_find_odds_number():
    """
    정수로 이루어진 배열 A안에 하나의 값을 제외하고 모두 짝수번 나타나고, 값 1개만 홀수번 나타남니다.
    홀수번 나타나는 하나의 값을 찾으세요
    """
    assert 3 == find_odds_number([1, 2, 3, 2, 3, 1, 3])
    assert 5 == find_odds_number([1, 1, 4, 4, 5, 5, 5, 5, 5, 4, 4])


def find_odds_number(arr):
    y = 0
    for v in arr:
        y ^= v

    return y
