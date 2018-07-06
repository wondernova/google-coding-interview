def test_two_sum():
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    ```
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    ```
    """

    nums = [2, 7, 11, 15]
    target = 9
    expected_answer = [0, 1]

    assert expected_answer == answer(nums, target)


def answer(nums: list, target: int):
    """

    """
    complement = dict()
    for i, num in enumerate(nums):

        if num in complement:
            return [complement[num], i]

        complement[target - num] = i
    return None
