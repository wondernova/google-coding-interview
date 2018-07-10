def test_anagram():
    assert anagram('python', 'typhon')
    assert anagram('heart', 'earth')
    assert anagram('silent', 'listen')
    assert anagram('William Shakespeare', 'I am a weakish speller')
    assert anagram('Dormitory', 'Dirty room')
    assert anagram('Astronomer', 'Moon starer')
    assert anagram('Conversation', 'Voices rant on')


def anagram(s1, s2):
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
