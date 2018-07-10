from unittest import TestCase


def sort(data):
    new_one = data[:]
    new_one.sort()
    return new_one


def test_bubble_sort():
    data = [2050, 0, -1, 20, 100, 99, 23, 20, -10, 3, 8, 7, 20.5, 3.5, -100]
    answer = sort(data)
    assert answer == bubble_sort(data)

    data = [1, 2, 3, 4, 5, 6]
    answer = sort(data)
    assert answer == bubble_sort(data)

    data = [6, 5, 4, 3, 2, 1]
    answer = sort(data)
    assert answer == bubble_sort(data)

    data = [10, 100, 100, 20, 30, 17, 0.5, 30, 10, -50, 100]
    answer = sort(data)
    assert answer == bubble_sort(data)

    data = [10]
    answer = sort(data)
    assert answer == bubble_sort(data)

    data = [20, 10]
    answer = sort(data)
    assert answer == bubble_sort(data)

    data = []
    answer = sort(data)
    assert answer == bubble_sort(data)


def bubble_sort(data):
    count = len(data) - 1
    while count >= 0:
        for j in range(count):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        count -= 1
    return data
