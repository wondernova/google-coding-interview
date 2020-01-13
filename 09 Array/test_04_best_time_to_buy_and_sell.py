def test_best_time_to_buy_and_sell_with_one_transaction():
    """
    array 가 주어지고, 단한번만의 거래 (transaction)을 할 수 있다
    즉 딱 한번만 사고, 팔수 있다
    수익을 가장 크게 하는 알고리즘을 구현하여라

    Input: [7, 1, 5, 3, 6, 4]
    Output : 5
    Explanation: day 2 (1)에 사서, day 5 (6)에 팔았음. 6-1=5
    """

    arr = [7, 1, 5, 3, 6, 4]
    assert my_answer(arr) == 5

    arr = [1]
    assert my_answer(arr) == 0

    arr = [1, 2, 3, 4, 5]
    assert my_answer(arr) == 4

    arr = [5, 4, 3, 2, 1]
    assert my_answer(arr) == 0

    arr = [17, 5, 3, 6, 2, 10, 4, 12]
    assert my_answer(arr) == 10


def my_answer(arr):
    min_value = arr[0]

    profit = 0
    for v in arr:
        if v < min_value:
            min_value = v

        profit = max(profit, v - min_value)
    return profit
