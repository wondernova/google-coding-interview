import numpy as np


def test_array_left_rotation():
    """
    https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

    A left rotation operation on an array shifts each of the array's elements  unit to the left.
    For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5],
    then the array would become [3, 4, 5, 1, 2].

    Given an array `a` of `n`  integers and a number, `d`, perform `d` left rotations on the array.
    Return the updated array to be printed as a single line of space-separated integers.
    """

    # Test 1
    arr = [1, 2, 3, 4, 5]
    d = 2
    expected = [3, 4, 5, 1, 2]
    answer = my_answer(arr, d)
    np.testing.assert_equal(expected, answer)

    # Test 2
    arr = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
    d = 10
    expected = [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77]
    answer = my_answer(arr, d)
    np.testing.assert_equal(expected, answer)


def my_answer(arr, d):
    return arr[d:] + arr[:d]
