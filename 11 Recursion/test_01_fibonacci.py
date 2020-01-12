from numpy.testing import assert_equal


def test_fibonacci():
    """
    피보나치는 다음과 같은 수열을 의미한다
        fibonacci : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
        index     : 0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11,  12
    """
    assert 0 == fib(0)
    assert 1 == fib(1)
    assert 1 == fib(2)
    assert 2 == fib(3)
    assert 3 == fib(4)
    assert 5 == fib(5)
    assert 8 == fib(6)
    assert 13 == fib(7)
    assert 21 == fib(8)
    assert 34 == fib(9)
    assert 222232244629420445529739893461909967206666939096499764990979600 == fib(300)

    assert 0 == fib_dp(0)
    assert 1 == fib_dp(1)
    assert 1 == fib_dp(2)
    assert 2 == fib_dp(3)
    assert 3 == fib_dp(4)
    assert 5 == fib_dp(5)
    assert 8 == fib_dp(6)
    assert 13 == fib_dp(7)
    assert 21 == fib_dp(8)
    assert 34 == fib_dp(9)
    assert 222232244629420445529739893461909967206666939096499764990979600 == fib_dp(300)

    assert_equal([0], fib_dp2(0))
    assert_equal([0, 1], fib_dp2(1))
    assert_equal([0, 1, 1], fib_dp2(2))
    assert_equal([0, 1, 1, 2], fib_dp2(3))
    assert_equal([0, 1, 1, 2, 3], fib_dp2(4))
    assert_equal([0, 1, 1, 2, 3, 5], fib_dp2(5))
    assert_equal([0, 1, 1, 2, 3, 5, 8], fib_dp2(6))
    assert_equal([0, 1, 1, 2, 3, 5, 8, 13], fib_dp2(7))


def fib(n):
    if not hasattr(fib, 'memoize'):
        fib.memoize = {}

    if n in fib.memoize:
        return fib.memoize[n]

    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1

    fib.memoize[n] = fib(n - 1) + fib(n - 2)
    return fib.memoize[n]


def fib_dp(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b

    return b


def fib_dp2(n):
    if n == 0:
        return [0]

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(1, n):
        dp[i + 1] = dp[i - 1] + dp[i]

    return dp
