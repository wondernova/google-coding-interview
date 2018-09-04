def test_longest_palindromic_substring():
    assert 'aba' == longest_palindrome('babad')
    assert 'bb' == longest_palindrome('bb')
    assert 'bb' == longest_palindrome('cbbd')
    assert 'anana' == longest_palindrome('banana')


def longest_palindrome(s):
    n = len(s)
    longest_sub = ''
    for i in range(n):
        # Odd Case
        sub = check_palindrome(s, i, i)
        if len(sub) >= len(longest_sub):
            longest_sub = sub

        # Even Case
        sub = check_palindrome(s, i, i + 1)
        if len(sub) >= len(longest_sub):
            longest_sub = sub

    return longest_sub


def check_palindrome(s, start, end):
    n = len(s)
    while start >= 0 and end < n and s[start] == s[end]:
        start -= 1
        end += 1

    return s[start + 1: end]
