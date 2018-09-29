import math


def test_catalan_number():
    # Formula
    assert 1 == catalan_formula(1)
    assert 2 == catalan_formula(2)
    assert 5 == catalan_formula(3)
    assert 14 == catalan_formula(4)
    assert 42 == catalan_formula(5)
    assert 132 == catalan_formula(6)
    assert 429 == catalan_formula(7)
    assert 1430 == catalan_formula(8)
    assert 4862 == catalan_formula(9)
    assert 16796 == catalan_formula(10)

    # Recursion
    assert 1 == catalan_recursion(1)
    assert 2 == catalan_recursion(2)
    assert 5 == catalan_recursion(3)
    assert 14 == catalan_recursion(4)
    assert 42 == catalan_recursion(5)
    assert 132 == catalan_recursion(6)
    assert 429 == catalan_recursion(7)
    assert 1430 == catalan_recursion(8)
    assert 4862 == catalan_recursion(9)
    assert 16796 == catalan_recursion(10)

    # Recursion
    assert 1 == catalan_dp(1)
    assert 2 == catalan_dp(2)
    assert 5 == catalan_dp(3)
    assert 14 == catalan_dp(4)
    assert 42 == catalan_dp(5)
    assert 132 == catalan_dp(6)
    assert 429 == catalan_dp(7)
    assert 1430 == catalan_dp(8)
    assert 4862 == catalan_dp(9)
    assert 16796 == catalan_dp(10)


def catalan_formula(n):
    return math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n))


def catalan_recursion(n):
    """
    Time Complexity: O(n^4)
    """
    if n == 0:
        return 1

    catalan = 0
    for i in range(1, n + 1):
        catalan += catalan_recursion(i - 1) * catalan_recursion(n - i)
    return catalan


def catalan_dp(n):
    """
    Time Complexity: O(n^2)
    """
    if n == 0:
        return 1

    if not hasattr(catalan_dp, 'memoize'):
        catalan_dp.memoize = dict()

    if n in catalan_dp.memoize:
        return catalan_dp.memoize[n]

    catalan = 0
    for i in range(1, n + 1):
        catalan += catalan_dp(i - 1) * catalan_dp(n - i)
    catalan_dp.memoize[n] = catalan
    return catalan
