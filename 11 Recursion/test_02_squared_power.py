def test_squared_power():
    assert 2 ** 10 == power(2, 10)
    assert 3 ** 5 == power(3, 5)
    assert 1 ** 1 == power(1, 1)
    assert 0 ** 1 == power(0, 1)
    assert 0 ** 10 == power(0, 10)
    assert 4 ** 39 == power(4, 39)
    assert 4 ** 37 == power(4, 37)
    assert 3 ** 21 == power(3, 21)


def power(x, n):
    if n <= 0:
        return 1

    if n % 2 == 0:
        return power(x ** 2, n / 2)
    else:
        return x * power(x ** 2, (n - 1) / 2)
