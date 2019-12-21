import itertools


def test_permutation():
    arr = 'ABC'

    # using itertools
    answer = [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
    assert answer == list(itertools.permutations(arr, r=2))

    # No Argument Method
    response = permute_no_arguments(arr)
    print()
    print(list(itertools.permutations(arr)))
    print(response)


def permute_no_arguments(arr):
    """
    permutation = n!/(n-r)!
    """
    if len(arr) <= 1:
        return arr
    perms = permute_no_arguments(arr[1:])
    word = arr[0]

    result = []
    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + word + perm[i:])

    return result

def permute(arr, l, r):
