import itertools


def test_permutation():
    arr = list('ABC')

    # using itertools
    answer = [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
    assert answer == list(itertools.permutations(arr, r=2))

    # Test01 - DFS Permutation
    answer = list(itertools.permutations(arr))
    assert set(answer) == set(permutation(arr))


def permutation(arr):
    def dfs(arr, start, res):
        n = len(arr)
        if start >= n - 1:
            res.append(tuple(arr))
            return res

        for i in range(start, n):
            arr[start], arr[i] = arr[i], arr[start]
            dfs(arr, start + 1, res)
            arr[start], arr[i] = arr[i], arr[start]

    res = []
    dfs(arr, 0, res)
    return res
