def test_01knapsack():
    """
    가방안에 물건을 capacity가 허용하는 안에서 (꽉 채울필요 없음) 가장 가치가 높은 물건들로 채워넣는다.
    이때 무게는 w 이고, 가치는 v 이다.

    이때 물건을 쪼갤수 있다면 factional knapsack problem이고 (greedy algorithm),
    물건을 쪼갤수 없는 경우에는 0-1 knapsack problem (dynamic programming) 이라고 한다.
    해당 문제는 0-1 knapsack problem 이다.

    w = weights
    v = values
    answer format: (maximum value, [weights...])
    """
    w = [1, 2, 4, 2, 5]
    v = [5, 3, 5, 3, 2]
    assert (16, [2, 4, 2, 1]) == knapsack_resursive(w, v, 10)

    w = [3, 2, 4, 1, 3, 2]
    v = [1, 2, 3, 1, 4, 3]
    assert (11, [2, 3, 1, 4]) == knapsack_resursive(w, v, 8)

    w = [2, 1, 7, 5, 3, 4]
    v = [6, 0, 5, 2, 2, 4]
    assert (13, [3, 7, 2]) == knapsack_resursive(w, v, 11)


def knapsack_resursive(w, v, capacity):
    def f(capacity, i, sack=[]):
        if i <= 0:
            return [0, sack]
        elif capacity <= 0:
            return [0, sack]

        r1 = f(capacity - w[i - 1], i - 1, sack + [w[i - 1]])
        r1[0] = v[i - 1] + r1[0]
        r2 = f(capacity, i - 1, sack)

        return max(r1, r2, key=lambda x: x[0])

    max_value, weights = f(capacity, len(w))
    return max_value, weights
