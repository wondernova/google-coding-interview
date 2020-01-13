from bisect import bisect_left

odd_data = [10, 20, 29, 30, 31, 40, 50]
even_data = [10, 20, 29, 30, 31, 40, 50, 60]


def get_answer(data, target):
    answer = bisect_left(data, target)
    return answer if answer < len(data) and data[answer] == target else -1


def test_odd_data():
    assert 0 == get_answer(odd_data, 10)
    assert 1 == get_answer(odd_data, 20)
    assert 2 == get_answer(odd_data, 29)
    assert 3 == get_answer(odd_data, 30)
    assert 4 == get_answer(odd_data, 31)
    assert 5 == get_answer(odd_data, 40)
    assert 6 == get_answer(odd_data, 50)
    assert -1 == get_answer(odd_data, 5150)
    assert -1 == get_answer(odd_data, 0)
    assert -1 == get_answer(odd_data, -3874)
    assert -1 == get_answer(odd_data, 11)
    assert -1 == get_answer(odd_data, 49)
    assert -1 == get_answer(odd_data, 22.1)
    assert -1 == get_answer(odd_data, 30.5)

    assert 0 == binary_search(odd_data, 10)
    assert 1 == binary_search(odd_data, 20)
    assert 2 == binary_search(odd_data, 29)
    assert 3 == binary_search(odd_data, 30)
    assert 4 == binary_search(odd_data, 31)
    assert 5 == binary_search(odd_data, 40)
    assert 6 == binary_search(odd_data, 50)
    assert -1 == binary_search(odd_data, 5150)
    assert -1 == binary_search(odd_data, 0)
    assert -1 == binary_search(odd_data, -3874)
    assert -1 == binary_search(odd_data, 11)
    assert -1 == binary_search(odd_data, 49)
    assert -1 == binary_search(odd_data, 22.1)
    assert -1 == binary_search(odd_data, 30.5)


def test_even_data():
    assert 0 == get_answer(even_data, 10)
    assert 1 == get_answer(even_data, 20)
    assert 2 == get_answer(even_data, 29)
    assert 3 == get_answer(even_data, 30)
    assert 4 == get_answer(even_data, 31)
    assert 5 == get_answer(even_data, 40)
    assert 6 == get_answer(even_data, 50)
    assert 7 == get_answer(even_data, 60)
    assert -1 == get_answer(even_data, 5150)
    assert -1 == get_answer(even_data, 0)
    assert -1 == get_answer(even_data, -3874)
    assert -1 == get_answer(even_data, 11)
    assert -1 == get_answer(even_data, 49)
    assert -1 == get_answer(even_data, 22.1)
    assert -1 == get_answer(even_data, 30.5)

    assert 0 == binary_search(even_data, 10)
    assert 1 == binary_search(even_data, 20)
    assert 2 == binary_search(even_data, 29)
    assert 3 == binary_search(even_data, 30)
    assert 4 == binary_search(even_data, 31)
    assert 5 == binary_search(even_data, 40)
    assert 6 == binary_search(even_data, 50)
    assert 7 == binary_search(even_data, 60)
    assert -1 == binary_search(even_data, 5150)
    assert -1 == binary_search(even_data, 0)
    assert -1 == binary_search(even_data, -3874)
    assert -1 == binary_search(even_data, 11)
    assert -1 == binary_search(even_data, 49)
    assert -1 == binary_search(even_data, 22.1)
    assert -1 == binary_search(even_data, 30.5)


def binary_search(data, target):
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
