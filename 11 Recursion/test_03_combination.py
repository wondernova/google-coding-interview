def test_combination():
    assert 4 == nCr(4, 3)
    assert 10 == nCr(5, 3)
    assert 1 == nCr(1, 1)
    assert 1 == nCr(2, 2)
    assert 45 == nCr(10, 2)


def nCr(n, r):
    if r == 0 or n == r:
        return 1

    return nCr(n - 1, r - 1) + nCr(n - 1, r)
