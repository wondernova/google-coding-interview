from numpy.testing import assert_equal


def test_sum_of_two_elements_in_array():
    """
    배열 A 안에서 2개의 elements의 합이 K가 되는 두개의 요소를 찾는다
    """

    # Brute Force
    assert [10, 30] == find_sum_brute_force([1, 3, 10, 5, 4, 20, 30], 40)
    assert [5, 3] == find_sum_brute_force([5, 3, 4, 10, 22, 7], 8)
    assert [4, 5] == find_sum_brute_force([0, 0, 15, 4, 8, 22, 3, 5], 9)

    # Sort
    assert [10, 30] == find_sort_sum([1, 3, 10, 5, 4, 20, 30], 40)
    assert [3, 5] == find_sort_sum([5, 3, 4, 10, 22, 7], 8)
    assert [4, 5] == find_sort_sum([0, 0, 15, 4, 8, 22, 3, 5], 9)

    # Hash
    assert {10, 30} == set(find_hash_sum([1, 3, 10, 5, 4, 20, 30], 40))
    assert {3, 5} == set(find_hash_sum([5, 3, 4, 10, 22, 7], 8))
    assert {4, 5} == set(find_hash_sum([0, 0, 15, 4, 8, 22, 3, 5], 9))


def find_sum_brute_force(arr, k):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                return [arr[i], arr[j]]
    return None


def find_sort_sum(arr, k):
    """
    배열 arr 이 정렬이 안되어 있기 때문에..
    Time Complexity: O(nlogn)
    Space Complexity: O(1)

    만약 배열이 정렬이 이미 되어 있고 sorted 함수를 제거한다면..
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    arr = sorted(arr)
    left, right = 0, len(arr) - 1

    while left < right:
        k_pred = arr[left] + arr[right]

        if k_pred == k:
            return [arr[left], arr[right]]
        elif k_pred < k:
            left += 1
        else:
            right -= 1


def find_hash_sum(arr, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    hash = dict()

    for i in range(len(arr)):
        if arr[i] in hash:
            return [hash[arr[i]], arr[i]]

        hash[k - arr[i]] = arr[i]
    return None
