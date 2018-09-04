from numpy.testing import assert_equal


def test_fibonacci():
    """
    피보나치는 다음과 같은 수열을 의미한다
        fibonacci : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
        index     : 0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11,  12
    """
    assert 0 == fib_last(0)
    assert 1 == fib_last(1)
    assert 1 == fib_last(2)
    assert 2 == fib_last(3)
    assert 3 == fib_last(4)
    assert 5 == fib_last(5)
    assert 8 == fib_last(6)
    assert 13 == fib_last(7)
    assert 21 == fib_last(8)
    assert 34 == fib_last(9)

    assert_equal([0], fib(0))
    assert_equal([0, 1], fib(1))
    assert_equal([0, 1, 1], fib(2))
    assert_equal([0, 1, 1, 2], fib(3))
    assert_equal([0, 1, 1, 2, 3], fib(4))
    assert_equal([0, 1, 1, 2, 3, 5], fib(5))
    assert_equal([0, 1, 1, 2, 3, 5, 8], fib(6))
    assert_equal([0, 1, 1, 2, 3, 5, 8, 13], fib(7))


def fib_last(n):
    a, b = 0, 1

    if n == 0:
        return 0
    if n == 1:
        return 1

    for i in range(1, n):
        a, b = b, a + b

    return b


def fib(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]

    arr = [0, 1]
    for i in range(1, n):
        arr.append(arr[-1] + arr[-2])
    return arr
