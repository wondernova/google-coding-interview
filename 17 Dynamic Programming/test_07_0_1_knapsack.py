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

    # 0/1 Recursive Knapsack with weights
    w = [1, 2, 4, 2, 5]
    v = [5, 3, 5, 3, 2]
    assert (16, [2, 4, 2, 1]) == knapsack_resursive(w, v, 10)

    w = [3, 2, 4, 1, 3, 2]
    v = [1, 2, 3, 1, 4, 3]
    assert (10, [2, 3, 1, 2]) == knapsack_resursive(w, v, 8)

    w = [2, 1, 7, 5, 3, 4]
    v = [6, 0, 5, 2, 2, 4]
    assert (12, [4, 3, 1, 2]) == knapsack_resursive(w, v, 11)

    w = [2, 1, 4, 3, 1, 4]
    v = [2, 2, 9, 0, 3, 5]
    assert (19, [4, 1, 4, 1]) == knapsack_resursive(w, v, 11)

    # 0/1 Recursive Knapsack with maximum value
    w = [1, 2, 4, 2, 5]
    v = [5, 3, 5, 3, 2]
    assert 16 == knapsack_max_value(w, v, 10, len(w))

    w = [3, 2, 4, 1, 3, 2]
    v = [1, 2, 3, 1, 4, 3]
    assert 10 == knapsack_max_value(w, v, 8, len(w))

    w = [2, 1, 7, 5, 3, 4]
    v = [6, 0, 5, 2, 2, 4]
    assert 12 == knapsack_max_value(w, v, 11, len(w))

    w = [2, 1, 4, 3, 1, 4]
    v = [2, 2, 9, 0, 3, 5]
    assert 19 == knapsack_max_value(w, v, 11, len(w))

    # 0/1 Knapsack with repeatable values
    w = [1, 2, 4, 2, 5]
    v = [3, 0, 0, 1, 0]
    assert [12, [1, 1, 1, 1]] == knapsack_repeat(w, v, 4)

    w = [1, 3, 4, 2, 5]
    v = [1, 4, 4, 2, 3]
    assert [14, [2, 3, 3, 3]] == knapsack_repeat(w, v, 11)

    w = [1, 3, 4, 2, 5]
    v = [0, 4, 5, 3, 6]
    assert [10, [2, 2, 3]] == knapsack_repeat(w, v, 7)

    w = [1, 3, 4, 2, 5]
    v = [1, 4, 7, 3, 8]
    assert [15, [5, 4]] == knapsack_repeat(w, v, 9)


def knapsack_resursive(w, v, capacity):
    def f(capacity, i, sack=[]):
        if i < 0:
            return [0, sack]
        elif w[i] > capacity:
            return f(capacity, i - 1, sack)

        r1 = f(capacity - w[i], i - 1, sack + [w[i]])
        r1[0] += v[i]
        r2 = f(capacity, i - 1, sack)

        return max(r1, r2, key=lambda x: x[0])

    max_value, weights = f(capacity, len(w) - 1)
    return max_value, weights


def knapsack_max_value(w, v, capacity, i):
    if i <= 0:
        return 0
    elif w[i - 1] > capacity:
        return knapsack_max_value(w, v, capacity, i - 1)

    return max(v[i - 1] + knapsack_max_value(w, v, capacity - w[i - 1], i - 1),
               knapsack_max_value(w, v, capacity, i - 1))


def knapsack_repeat(w, v, capacity):
    def f(capacity, i, sack=[]):
        if i <= 0:
            return [0, sack]
        elif w[i - 1] > capacity:
            return f(capacity, i - 1, sack)

        r1 = f(capacity - w[i - 1], i - 1, sack + [w[i - 1]])
        r1[0] += v[i - 1]
        r2 = f(capacity - w[i - 1], i, sack + [w[i - 1]])
        r2[0] += v[i - 1]
        r3 = f(capacity, i - 1, sack)

        return max(r1, r2, r3, key=lambda x: x[0])

    return f(capacity, len(w))
