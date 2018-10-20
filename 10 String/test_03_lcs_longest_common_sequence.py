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
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    lcs = ''
    i, j = n, m
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            lcs = s1[i - 1] + lcs
            i -= 1
            j -= 1
    return lcs
