def test_contain_string():
    """
    문자열 A안에 문자열 B가 존재하는지 확인하는 함수를 만든다.
    예를 들어..

        A = 'zxabcde', B = 'abc'

    결과는 인덱스 2 가 리턴되야 한다.
    """
    assert 2 == contain_brute_force('zxabcde', 'abc')
    assert 3 == contain_brute_force('abeabc', 'abc')
    assert 0 == contain_brute_force('abcdefg', 'abc')
    assert 0 == contain_brute_force('abc', 'abc')
    assert 5 == contain_brute_force('123456', '6')
    assert 4 == contain_brute_force('123456', '56')


def contain_brute_force(a, b):
    """
    Time Complexity: O( (n -m) * m) -> O(n * m)
    Space Complexity: O(1)
    """
    n, m = len(a), len(b)

    for i in range(n - m + 1):
        j = 0
        while j < m:
            if a[i + j] != b[j]:
                break
            j += 1

        if j == m:
            return i
    return -1
