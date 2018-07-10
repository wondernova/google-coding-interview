def test_random_note():
    """
    https://www.hackerrank.com/challenges/ctci-ransom-note/problem
    """
    megazine = 'give me one grand today night'.split(' ')
    note = 'give one grand today'.split(' ')
    answer = my_answer(megazine, note)
    assert 'Yes' == answer

    megazine = 'two times three is not four'.split(' ')
    note = 'two times two is four'.split(' ')
    answer = my_answer(megazine, note)
    assert 'No' == answer


def my_answer(magazine, note):
    from collections import Counter

    if (Counter(note) - Counter(magazine)) == dict():
        return 'Yes'
    return 'No'
