def sort(data):
    new_one = data[:]
    new_one.sort()
    return new_one


def test_binary_insertion_sort():
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    answer = sort(data)
    assert answer == binary_insertion_sort(data)

    data = [2050, 0, -1, 20, 100, 99, 23, 20, -10, 3, 8, 7, 20.5, 3.5, -100]
    answer = sort(data)
    assert answer == binary_insertion_sort(data)

    data = [1, 2, 3, 4, 5, 6]
    answer = sort(data)
    assert answer == binary_insertion_sort(data)

    data = [6, 5, 4, 3, 2, 1]
    answer = sort(data)
    assert answer == binary_insertion_sort(data)

    data = [10, 100, 100, 20, 30, 17, 0.5, 30, 10, -50, 100]
    answer = sort(data)
    assert answer == binary_insertion_sort(data)

    data = [50, 10, 10, 10, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]
    answer = sort(data)
    assert answer == binary_insertion_sort(data)

    data = [10]
    answer = sort(data)
    assert answer == binary_insertion_sort(data)

    data = [20, 10]
    answer = sort(data)
    assert answer == binary_insertion_sort(data)

    data = []
    answer = sort(data)
    assert answer == binary_insertion_sort(data)


def binary_insertion_sort(data):
    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            continue

        left = 0
        right = i
        while left < right:
            mid = (left + right) // 2

            if data[i] > data[mid]:
                left = mid + 1
            else:
                right = mid

        j = i
        while j > left:
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1
    return data
