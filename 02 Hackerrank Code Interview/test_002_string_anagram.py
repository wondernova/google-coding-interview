def test_anagram():
    """
    https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
    """
    arr1 = list('cde')
    arr2 = list('abc')
    expected = 4
    answer = my_answer(arr1, arr2)
    assert expected == answer

    answer = my_answer(list('fcrxzwscanmligyxyvym'), list('jxwtrhvujlmrpdoqbisbwhmgpmeoke'))
    expected = 30
    assert expected == answer


def my_answer(a, b):
    buf = dict()

    for s in a:
        buf.setdefault(s, 0)
        buf[s] += 1

    for s in b:
        buf.setdefault(s, 0)
        buf[s] -= 1

    buf = list(filter(lambda x: x != 0, buf.values()))
    buf = list(map(lambda x: abs(x), buf))
    return sum(buf)
