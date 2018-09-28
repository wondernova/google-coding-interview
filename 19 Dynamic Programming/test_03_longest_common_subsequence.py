from pprint import pprint


def test_longest_common_subsequence():
    # Recursion
    assert 'ADH' == lcs_recursion('ABCDGH', 'AEDFHR')
    assert 'aabc' == lcs_recursion('aabcd', 'aeabc')
    assert 'abbcd' == lcs_recursion('abbcde', 'zazmabzbzczd')
    assert 'a13579' == lcs_recursion('a13579', 'a13579')
    assert 'baabbaabb' == lcs_recursion('abaabbaabcba', 'baacbcbaabb')

    # Dynamic Programming
    assert 'ADH' == lcs_dp('ABCDGH', 'AEDFHR')
    assert 'aabc' == lcs_dp('aabcd', 'aeabc')
    assert 'abbcd' == lcs_dp('abbcde', 'zazmabzbzczd')
    assert 'a13579' == lcs_dp('a13579', 'a13579')
    assert 'baabbaabb' == lcs_dp('abaabbaabcba', 'baacbcbaabb')


def lcs_recursion(a, b, i=0, j=0, lcs=''):
    """
    문자열이 서로 일치하지 않는다면, recursion의 branch가 2개로 갈라지게 됩니다.
    이때 Time Complexity는 O(2^n) 이 되게 됩니다.
    """
    if i >= len(a) or j >= len(b):
        return lcs

    if a[i] == b[j]:
        return lcs_recursion(a, b, i + 1, j + 1, lcs + a[i])
    else:
        return max(lcs_recursion(a, b, i + 1, j, lcs),
                   lcs_recursion(a, b, i, j + 1, lcs),
                   key=len)


def lcs_dp(a, b):
    n, m = len(a), len(b)
    table = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])
    string = ''
    i, j = n, m
    while i >= 0 and j >= 0:
        if table[i][j] == table[i - 1][j]:
            i -= 1
        elif table[i][j] == table[i][j - 1]:
            j -= 1
        else:
            assert a[i - 1] == b[j - 1]
            string = a[i - 1] + string
            i -= 1
            j -= 1
    return string
