def sort(data):
    new_one = data[:]
    new_one.sort()
    return new_one


def test_insertion_sort():
    data = [2050, 0, -1, 20, 100, 99, 23, 20, -10, 3, 8, 7, 20.5, 3.5, -100]
    answer = sort(data)
    assert answer == insertion_sort(data)

    data = [1, 2, 3, 4, 5, 6]
    answer = sort(data)
    assert answer == insertion_sort(data)

    data = [6, 5, 4, 3, 2, 1]
    answer = sort(data)
    assert answer == insertion_sort(data)

    data = [10, 100, 100, 20, 30, 17, 0.5, 30, 10, -50, 100]
    answer = sort(data)
    assert answer == insertion_sort(data)

    data = [10]
    answer = sort(data)
    assert answer == insertion_sort(data)

    data = [20, 10]
    answer = sort(data)
    assert answer == insertion_sort(data)

    data = []
    answer = sort(data)
    assert answer == insertion_sort(data)


def insertion_sort(data):
    for end in range(1, len(data)):
        end_value = data[end]
        count = end
        while count > 0 and data[count - 1] >= end_value:
            data[count] = data[count - 1]
            count -= 1
        data[count] = end_value
    return data
