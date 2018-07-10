def sort(data):
    new_one = data[:]
    new_one.sort()
    return new_one


def test_selection_sort():
    data = [2050, 0, -1, 20, 100, 99, 23, 20, -10, 3, 8, 7, 20.5, 3.5, -100]
    answer = sort(data)
    assert answer == selection_sort(data)

    data = [1, 2, 3, 4, 5, 6]
    answer = sort(data)
    assert answer == selection_sort(data)

    data = [6, 5, 4, 3, 2, 1]
    answer = sort(data)
    assert answer == selection_sort(data)

    data = [10, 100, 100, 20, 30, 17, 0.5, 30, 10, -50, 100]
    answer = sort(data)
    assert answer == selection_sort(data)

    data = [10]
    answer = sort(data)
    assert answer == selection_sort(data)

    data = [20, 10]
    answer = sort(data)
    assert answer == selection_sort(data)

    data = []
    answer = sort(data)
    assert answer == selection_sort(data)


def selection_sort(data):
    N = len(data)
    for end_point in range(N - 1, 0, -1):
        max_pos = 0
        for i in range(0, end_point + 1):
            if data[max_pos] < data[i]:
                max_pos = i
        data[end_point], data[max_pos] = data[max_pos], data[end_point]
    return data
