def test_factorial():
    """
    Factorial은 n과 1사이의 모든 정수를 곱한것이다.
    n! = n*(n-1)!
    1! = 1
    0! = 1
    """

    # Simple Recursive Factorial
    assert 1 == factorial_simple(0)
    assert 1 == factorial_simple(1)
    assert 2 == factorial_simple(2)
    assert 6 == factorial_simple(3)
    assert 24 == factorial_simple(4)
    assert 120 == factorial_simple(5)
    assert 720 == factorial_simple(6)
    assert 5040 == factorial_simple(7)

    # Simple Recursive Factorial
    assert 1 == factorial_dp(0)
    assert 1 == factorial_dp(1)
    assert 2 == factorial_dp(2)
    assert 6 == factorial_dp(3)
    assert 24 == factorial_dp(4)
    assert 120 == factorial_dp(5)
    assert 720 == factorial_dp(6)
    assert 5040 == factorial_dp(7)


def factorial_simple(n):
    """
    Recursion에 대한 Time complexity

        T(n) = n x T(n-1) = O(n)

    Time complexity 가 O(n)이기 때문에 DP로 딱히 optimize할 수 있는게 없어 보인다.
    """
    assert n >= 0

    if n == 0:
        return 1
    elif n == 1:
        return 1

    return n * factorial_simple(n - 1)


def factorial_dp(n):
    """
    한번 계산할때는 사실 도움은 안되나..
    만약 이전에 계산한 값이 있다면, DP를 통해 이전에 계산한 값을 저장한 테이블에서 가져와서 연산량을 줄일수 있습니다.
    """
    if not hasattr(factorial_dp, 'memoize'):
        factorial_dp.memoize = {}

    if n in factorial_dp.memoize:
        return factorial_dp.memoize[n]

    if n == 0:
        return 1
    elif n == 1:
        return 1

    return n * factorial_dp(n - 1)
