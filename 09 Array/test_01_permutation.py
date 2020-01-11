import itertools


def test_permutation():
    arr = list('ABC')

    # using itertools
    answer = [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
    assert answer == list(itertools.permutations(arr, r=2))

    # Test01 - DFS Permutation
    answer = list(itertools.permutations(arr))
    print(set(answer))
    assert set(answer) == set(permutation(arr))


def permutation(arr):
    if not arr:
        return arr

    response = []

    def dfs(start_idx):
        n = len(arr)
        if start_idx == n - 1:
            response.append(tuple(arr[:]))

        for i in range(start_idx, n):
            arr[start_idx], arr[i] = arr[i], arr[start_idx]
            dfs(start_idx + 1)
            arr[start_idx], arr[i] = arr[i], arr[start_idx]

    dfs(0)
    return response
