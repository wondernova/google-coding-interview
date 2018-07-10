def sort(data):
    new_one = data[:]
    new_one.sort()
    return new_one


def test_shell_sort():
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    answer = sort(data)
    assert answer == shell_sort(data)

    data = [2050, 0, -1, 20, 100, 99, 23, 20, -10, 3, 8, 7, 20.5, 3.5, -100]
    answer = sort(data)
    assert answer == shell_sort(data)

    data = [1, 2, 3, 4, 5, 6]
    answer = sort(data)
    assert answer == shell_sort(data)

    data = [6, 5, 4, 3, 2, 1]
    answer = sort(data)
    assert answer == shell_sort(data)

    data = [10, 100, 100, 20, 30, 17, 0.5, 30, 10, -50, 100]
    answer = sort(data)
    assert answer == shell_sort(data)

    data = [10]
    answer = sort(data)
    assert answer == shell_sort(data)

    data = [20, 10]
    answer = sort(data)
    assert answer == shell_sort(data)

    data = []
    answer = sort(data)
    assert answer == shell_sort(data)


def shell_sort(data):
    N = len(data)
    sub_count = N // 2
    while sub_count > 0:
        gap_insertion_sort(data, sub_count)
        sub_count //= 2
    return data


def gap_insertion_sort(data, gap):
    N = len(data)
    for end_point in range(gap, N, gap):
        current_value = data[end_point]
        position = end_point

        while position - gap >= 0 and data[position - gap] > current_value:
            data[position] = data[position - gap]
            position -= gap

        data[position] = current_value
        # print data, 'position:%d current_value:%d, end_point:%d' % (position, current_value, end_point)
