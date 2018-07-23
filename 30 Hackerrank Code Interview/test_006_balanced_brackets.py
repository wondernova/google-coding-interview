def test_balanced_brackets():
    """
    https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

    다음과 같이 3가지 종류의 brackets이 있다.
      -> (, )
      -> {, }
      -> [, ]

    만약 열리고 닫히는 쌍의 brackets이 서로 다르면 not balanced brackets 라고 말한다.
    예를 들어서 다음은 not balanced brackets 이다.
    ```
        {[(])}
    ```

    예를 들어서 다음은 balanced brackets 이다.
    ```
        []
        {}
        ()
        []{}()
        [({})]{}()
        ({(){}[])[]
    ```
    """

    assert your_answer('{[()]}')
    assert not your_answer('{[(])}')
    assert not your_answer('{[(')
    assert your_answer('{{[[(())]]}}')


def your_answer(string):
    buf = list()

    close_tokens = {'}': '{',
                    ']': '[',
                    ')': '('}
    open_tokens = close_tokens.values()

    for s in string:
        if s in open_tokens:
            buf.append(s)
        else:
            if not buf:
                return False

            elif close_tokens[s] != buf.pop():
                return False
    if buf:
        return False
    return True
