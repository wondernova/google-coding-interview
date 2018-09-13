def test_word_break():
    # Recursion
    assert word_break('applepenapple', ['apple', 'pen', 'appolo'])
    assert word_break('incredibleai', ['incredible', 'ai'])
    assert word_break('abdogspamabandon', ['ab', 'dog', 'spam', 'abandon', 'micro', 'street', 'apoch'])
    assert False == word_break('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])
    assert False == word_break('abcababd', ['abc', 'cad'])
    assert False == word_break('aaaaaaaaa', ['aa'])
    assert False == word_break('abcdefabcde', ['abcdef'])


def word_break(s, words):
    n = len(s)
    words = set(words)
    memoize = dict()

    def f(start):
        if start >= n:
            return True

        if memoize.get(start) is not None:
            print('MEMOIZE', start, memoize[start], s)
            return memoize[start]

        for end in range(start + 1, n + 1):
            if s[start: end] in words and f(end):
                memoize[start] = True
                return True

        memoize[start] = False
        return False

    return f(0)
