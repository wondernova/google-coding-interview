from pprint import pprint


def test_longest_common_subsequence():
    """
    LCS는 두개의 문제로 나뉘어 집니다.
    Longest Common Substring 그리고 Longest Common Subsequence 이 두개로 나뉘어 지며, 서로 다른 문제입니다.
    두개의 차이점은 연속성에 있습니다.

    Longest Common Substring (연속적)
        ABCDHEF, BCDEF -> BCD

    Longest Common Subsequence (비연속적)
        ABCDHEF, BCDEF -> BCDEF

    1. String1[n], String2[k]가 같다면 : [n, k] == [n-1, k-1] + 1
    2. String1[n], String2[k]가 다르면 : [n, k] == [n-1, k]와 [n, k-1] 중 큰 값
    """

    # Recursion
    assert 'ADH' == lcs_recursion('ABCDGH', 'AEDFHR')
    assert 'aabc' == lcs_recursion('aabcd', 'aeabc')
    assert 'abbcd' == lcs_recursion('abbcde', 'zazmabzbzczd')

    # Dynamic Programming
    assert 'ADH' == lcs_dp('ABCDGH', 'AEDFHR')
    assert 'aabc' == lcs_dp('aabcd', 'aeabc')
    assert 'abbcd' == lcs_dp('abbcde', 'zazmabzbzczd')


def lcs_recursion(s1: str, s2: str):
    if not s1 or not s2:
        return ''

    if s1[0] == s2[0]:
        return s1[0] + lcs_recursion(s1[1:], s2[1:])
    else:
        return max(lcs_recursion(s1, s2[1:]),
                   lcs_recursion(s1[1:], s2),
                   key=len)


def lcs_dp(s1: str, s2: str):
    m, n = len(s1), len(s2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])

    i, j = len(s1), len(s2)
    result = ''
    while i != 0 and j != 0:
        if table[i][j] == table[i - 1][j]:
            i -= 1
        elif table[i][j] == table[i][j - 1]:
            j -= 1
        else:
            assert s1[i - 1] == s2[j - 1]
            result = s1[i - 1] + result
            i -= 1
            j -= 1
    return result
