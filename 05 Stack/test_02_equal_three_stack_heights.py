def test_equal_three_stacks():
    """
    3개의 stacks이 주어집니다. 이때 동일한 높이를 갖는 height를 리턴시키세요
    """

    l = [[3, 4, 5],
         [10, 2, 4],
         [1, 5, 4, 2, 0, 0]]
    assert 12 == equalStacks(*l)

    l = [[0, 0, 0],
         [5, 2, 1, 1, 1, 0, 0, 0],
         [10, 1, 4, 7]]
    assert 0 == equalStacks(*l)

    l = [[5, 4, 3, 2, 1],
         [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [3, 2, 1, 3, 4]]
    assert 9 == equalStacks(*l)

    l = [[2, 1, 1, 1, 1],
         [7, 3],
         [1, 3, 1]]
    assert 0 == equalStacks(*l)

    l = [[3, 4, 2, 2, 1, 3],
         [1, 4, 2, 5],
         [7]]
    assert 7 == equalStacks(*l)

    l = [[0],
         [1, 4, 2, 5],
         []]
    assert 0 == equalStacks(*l)

    l = [[5],
         [1, 4, 2, 5],
         []]
    assert 0 == equalStacks(*l)


def equalStacks(a, b, c):
    stacks = [a, b, c]
    sums = [sum(a), sum(b), sum(c)]

    while not (sums[0] == sums[1] == sums[2]):
        idx = max((0, 1, 2), key=lambda i: sums[i] - stacks[i][-1] if sums[i] > 0 else -1)
        if idx < 0:
            break

        sums[idx] -= stacks[idx].pop()

    return sums[0]
