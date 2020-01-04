def test_longest_substring_without_repeating_characters():
    """
    Given a string, find the length of the longest substring without repeating characters.
    ```
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    ```
    """
    question = 'abcabcbb'
    expected = 3  # 'abc'
    assert expected == my_answer(question)

    question = 'abcabcdabcdef'
    expected = 6  # 'abcdef'
    assert expected == my_answer(question)

    question = 'abcdefgabcdabc'
    expected = 7  # 'abcdefg'
    assert expected == my_answer(question)

    question = 'bbbbb'
    expected = 1  # 'b'
    assert expected == my_answer(question)

    question = 'pwwkew'
    expected = 3  # 'wke'
    assert expected == my_answer(question)

    question = 'dvdf'
    expected = 3  # 'vdf'
    assert expected == my_answer(question)


def my_answer(s):
    start = max_length = 0
    duplicates = dict()

    for i, c in enumerate(s):
        if c in duplicates and start <= duplicates[c]:
            start = duplicates[c] + 1
        else:
            max_length = max(i - start + 1, max_length)

        duplicates[c] = i
    return max_length
