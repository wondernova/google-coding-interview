def test_staircase():
    """
    어떤 사람이 점프를 해서 최고 6칸의 계단을 한꺼번에 오를수 있습니다.
    올라갈수 있는 경우의 수가 1~6칸 이라면 n-th 계단을 올라가는데 모든 경우의 수를 구하는 함수를 작성하세요

    계단의 시작점이 0번이고, 계단이 올라감에 따라 순차적으로 증가하여 n번째 계단까지 있습니다.
    이 경우 예제는 다음과 같습니다.
    n=0 -> 1 [0]
    n=1 -> 1 [1]
    n=2 -> 2 [1, 2], [2]
    n=3 -> 4 [1, 2, 3], [1, 3], [2, 3], [3]
    n=4 -> 8 [1, 2, 3, 4,], [1, 2, 4], [1, 3, 4], [1, 4], [2, 3, 4], [2, 4], [3, 4], [4]
    """
    # Recursive Method
    assert 1 == num_ways(0)
    assert 1 == num_ways(1)
    assert 2 == num_ways(2)
    assert 4 == num_ways(3)
    assert 8 == num_ways(4)
    assert 16 == num_ways(5)
    assert 32 == num_ways(6)
    assert 63 == num_ways(7)

    # Dynamic Programming Method
    assert 1 == num_ways_dp(0)
    assert 1 == num_ways_dp(1)
    assert 2 == num_ways_dp(2)
    assert 4 == num_ways_dp(3)
    assert 8 == num_ways_dp(4)
    assert 16 == num_ways_dp(5)
    assert 32 == num_ways_dp(6)
    assert 63 == num_ways_dp(7)
    assert num_ways(610) == num_ways_dp(610)


def num_ways(n):
    if n <= 1:
        return 1

    if not hasattr(num_ways, 'memoize'):
        num_ways.memoize = dict()

    if n not in num_ways.memoize:
        i, sum = 1, 0
        while i <= 6 and n >= i:
            sum += num_ways(n - i)
            i += 1
        num_ways.memoize[n] = sum

    return num_ways.memoize[n]


def num_ways_dp(n):
    dp = [1] * max(n + 1, 2)

    for i in range(2, n + 1):
        j, sum = max(i - 6, 0), 0

        while j < i:
            sum += dp[j]
            j += 1
        dp[i] = sum
    return dp[-1]
