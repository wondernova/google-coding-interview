def test_anagram():
    """
    글자들을 재배열해서 다른 글자가 완성이 될 수 있으면 anagram이다.
    anagram이 되는지 안되는지 체크하는 알고리즘을 만들어라
    """
    assert anagram('python', 'typhon')
    assert anagram('heart', 'earth')
    assert anagram('silent', 'listen')
    assert anagram('William Shakespeare', 'I am a weakish speller')
    assert anagram('Dormitory', 'Dirty room')
    assert anagram('Astronomer', 'Moon starer')
    assert anagram('Conversation', 'Voices rant on')


def anagram_backup(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    check = list(s2)
    correct = True
    for c in s1:
        pos = 0
        found = False
        for i in range(len(s2)):
            if c == check[i]:
                found = True
                pos = i
        if found:
            check[pos] = None
        else:
            correct = False
    return correct


def anagram(s1, s2):
    buf = {}

    for s in s1:
        buf.setdefault(s, 0)
        buf[s] += 1

    for s in s2:
        buf.setdefault(s, 0)
        buf[s] -= 1

    if ' ' in buf:
        del buf[' ']
    return not bool(sum(buf.values()))
