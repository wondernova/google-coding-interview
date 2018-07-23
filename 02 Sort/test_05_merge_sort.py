def sort(data):
    new_one = data[:]
    new_one.sort()
    return new_one


def test_merge_sort():
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    answer = sort(data)
    assert answer == merge_sort(data)

    data = [2050, 0, -1, 20, 100, 99, 23, 20, -10, 3, 8, 7, 20.5, 3.5, -100]
    answer = sort(data)
    assert answer == merge_sort(data)

    data = [1, 2, 3, 4, 5, 6]
    answer = sort(data)
    assert answer == merge_sort(data)

    data = [6, 5, 4, 3, 2, 1]
    answer = sort(data)
    assert answer == merge_sort(data)

    data = [10, 100, 100, 20, 30, 17, 0.5, 30, 10, -50, 100]
    answer = sort(data)
    assert answer == merge_sort(data)

    data = [10]
    answer = sort(data)
    assert answer == merge_sort(data)

    data = [20, 10]
    answer = sort(data)
    assert answer == merge_sort(data)

    data = []
    answer = sort(data)
    assert answer == merge_sort(data)


def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left, right = data[:mid], data[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

    return data
