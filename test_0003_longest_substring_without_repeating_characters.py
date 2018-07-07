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
    answer = my_answer(question)
    assert expected == answer

    question = 'bbbbb'
    expected = 1  # 'b'
    answer = my_answer(question)
    assert expected == answer

    question = 'pwwkew'
    expected = 3  # 'wke'
    answer = my_answer(question)
    assert expected == answer


def my_answer(s):
    string = s
    start = max_length = 0
    duplicates = dict()

    for i, s in enumerate(string):
        if string[i] in duplicates and start <= duplicates[s]:
            start = duplicates[s] + 1
        else:
            max_length = max(max_length, i - start + 1)

        duplicates[s] = i
    return max_length
