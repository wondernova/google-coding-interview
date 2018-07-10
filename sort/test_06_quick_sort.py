def sort(data):
    new_one = data[:]
    new_one.sort()
    return new_one


def test_quick_sort():
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    answer = sort(data)
    assert answer == quick_sort(data)

    data = [2050, 0, -1, 20, 100, 99, 23, 20, -10, 3, 8, 7, 20.5, 3.5, -100]
    answer = sort(data)
    assert answer == quick_sort(data)

    data = [1, 2, 3, 4, 5, 6]
    answer = sort(data)
    assert answer == quick_sort(data)

    data = [6, 5, 4, 3, 2, 1]
    answer = sort(data)
    assert answer == quick_sort(data)

    data = [10, 100, 100, 20, 30, 17, 0.5, 30, 10, -50, 100]
    answer = sort(data)
    assert answer == quick_sort(data)

    data = [50, 10, 10, 10, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]
    answer = sort(data)
    assert answer == quick_sort(data)

    data = [10]
    answer = sort(data)
    assert answer == quick_sort(data)

    data = [20, 10]
    answer = sort(data)
    assert answer == quick_sort(data)

    data = []
    answer = sort(data)
    assert answer == quick_sort(data)


def quick_sort(data):
    less = []
    equal = []
    more = []

    if len(data) > 1:
        pivot = data[0]

        for v in data:
            if v < pivot:
                less.append(v)
            elif v == pivot:
                equal.append(v)
            elif v > pivot:
                more.append(v)

        return quick_sort(less) + equal + quick_sort(more)
    return data
