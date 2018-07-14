def test_random_note():
    """
    https://www.hackerrank.com/challenges/ctci-ransom-note/problem

    납치범이 글자를 손으로 집접 쓰지 않고.. 책에서 가져와서 몸값을 요구하는 편지를 쓰려고 한다.
    이때 책에 있는 단어들을 갖고서 원하는 문장을 만들수 있는지 없는지 알아내는 함수를 만드시오
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
