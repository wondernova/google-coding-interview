def test_robin_karp():
    """
    문자열 B가 문자열 A안에 존재하는지 확인하는 다른 방법은 Robin Karp를 사용하는 방법입니다.
    Robin Karp를 해시기술을 사용하여 brute force 였을때 O(n*m) 의 복잡도를 O(n + m) 으로 낮출수 있습니다.

    O(1) 으로 처리될 수 있는 해시기술을 만드는것이 관건입니다.
    """
    assert 2 == robin_karp_simple('zxabcdef', 'abc')
    assert 0 == robin_karp_simple('abcabdef', 'abc')
    assert 3 == robin_karp_simple('aaaabc', 'abc')
    assert 4 == robin_karp_simple('abababc', 'abc')
    assert 7 == robin_karp_simple('abcdefgz', 'z')
    assert 0 == robin_karp_simple('zabcdefg', 'z')
    assert -1 == robin_karp_simple('ddedaddbdd', 'ddd')
    assert -1 == robin_karp_simple('ddedaddbdd', 'z')


def robin_karp_simple(a, b):
    """
    Time Complexity: O(n - m + 1) -> O(n)
    Space Complexity: O(1)
    """
    n, m = len(a), len(b)
    hash_b = hash(b)
    for i in range(n - m + 1):
        if hash(a[i:i + m]) == hash_b:
            return i
    return -1
0