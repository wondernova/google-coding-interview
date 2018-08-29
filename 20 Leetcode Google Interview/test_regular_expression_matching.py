def test_regex_match():
    """
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.

     The matching should cover the entire input string (not partial).
    """

    # Recursion
    assert not match_recursive('aa', 'a')
    assert not match_recursive('a', 'ab')
    assert not match_recursive('aaaaa', 'aaaa')
    assert not match_recursive('aaaa', 'aaab')
    assert match_recursive('aa', 'a*')
    assert match_recursive('ab', '.*')
    assert match_recursive('abcd', '.*')
    assert match_recursive('aab', 'c*a*b*')
    assert match_recursive('aabcc', '.*cc')
    assert match_recursive('aa', 'a*b*c*')
    assert match_recursive('abcdef', '......')
    assert match_recursive('aaaaaaa', 'a*b*c*')
    assert match_recursive('aaaab', 'a*.*b')

    # Dynamic Programming
    assert not match_dp('aa', 'a')
    assert not match_dp('a', 'ab')
    assert not match_dp('aaaaa', 'aaaa')
    assert not match_dp('aaaa', 'aaab')
    assert match_dp('aa', 'a*')
    assert match_dp('ab', '.*')
    assert match_dp('abcd', '.*')
    assert match_dp('aab', 'c*a*b*')
    assert match_dp('aabcc', '.*cc')
    assert match_dp('aa', 'a*b*c*')
    assert match_dp('abcdef', '......')
    assert match_dp('aaaaaaa', 'a*b*c*')
    assert match_dp('aaaab', 'a*.*b')


def match_recursive(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return ((first_match and match_recursive(text[1:], pattern)) or
                match_recursive(text, pattern[2:]))

    return first_match and match_recursive(text[1:], pattern[1:])


def match_dp(text, pattern):
    memoize = {}

    def dp(i, j):
        if (i, j) not in memoize:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}

                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    ans = dp(i, j + 2) or (dp(i + 1, j) and first_match)
                else:
                    ans = first_match and dp(i + 1, j + 1)
            memoize[i, j] = ans

        return memoize[i, j]

    return dp(0, 0)
