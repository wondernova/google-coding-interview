def test_reverse_string():
    """
    O(n/2) 로 끝낼수 있는 방법으로 문제를 해결해야 한다.
    """

    # Swap
    s = 'abcdefg'
    assert s[::-1] == swap(s)

    s = '1234567'
    assert s[::-1] == swap(s)

    s = 'ab'
    assert s[::-1] == swap(s)

    s = 'abc'
    assert s[::-1] == swap(s)

    s = 'd'
    assert s[::-1] == swap(s)

    # XOR

    s = 'abcdefg'
    assert s[::-1] == xor(s)
    print(xor(s))

    s = '1234567'
    assert s[::-1] == xor(s)

    s = 'ab'
    assert s[::-1] == xor(s)

    s = 'abc'
    assert s[::-1] == xor(s)

    s = 'd'
    assert s[::-1] == xor(s)


def swap(s):
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)


def xor(s):
    l = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        l[left] = ord(s[left]) ^ ord(s[right])
        l[left], l[right] = chr(ord(s[left]) ^ l[left]), chr(ord(s[right]) ^ l[left])
        left += 1
        right -= 1

    return ''.join(l)
