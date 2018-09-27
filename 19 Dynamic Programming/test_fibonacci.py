def test_fibonacci_with_dp():
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
    assert 55 == fib(10)


def fib(n):
    assert n >= 0
    if n <= 1:
        return n

    a, b, sum = 0, 1, 0
    for i in range(n - 1):
        sum = a + b
        a, b = b, sum

    return sum
