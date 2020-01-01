def test_fibonacci_with_dp():
    # Dynamic Programming
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

    # Recursion with Memoize
    assert 0 == fib_recursive(0)
    assert 1 == fib_recursive(1)
    assert 1 == fib_recursive(2)
    assert 2 == fib_recursive(3)
    assert 3 == fib_recursive(4)
    assert 5 == fib_recursive(5)
    assert 8 == fib_recursive(6)
    assert 13 == fib_recursive(7)
    assert 21 == fib_recursive(8)
    assert 34 == fib_recursive(9)
    assert 55 == fib_recursive(10)


def fib(n):
    assert n >= 0
    if n <= 1:
        return n

    a, b, sum = 0, 1, 0
    for i in range(n - 1):
        sum = a + b
        a, b = b, sum

    return sum


def fib_recursive(n):
    assert n >= 0
    if n <= 1:
        return n

    if not hasattr(fib_recursive, 'memoize'):
        fib_recursive.memoize = dict()

    if n in fib_recursive.memoize:
        return fib_recursive.memoize[n]

    result = fib_recursive(n - 1) + fib_recursive(n - 2)
    fib_recursive.memoize[n] = result
    return result
