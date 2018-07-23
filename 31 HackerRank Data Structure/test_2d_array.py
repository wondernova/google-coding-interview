def hourglassSum(arr):
    if arr is None or not arr:
        raise Exception('arr should have 2 dimensional data')
    h, w = len(arr), len(arr[0])

    response = list()
    for i in range(h - 2):
        for j in range(w - 2):
            elements = [arr[i][j], arr[i][j + 1], arr[i][j + 2],
                        arr[i + 1][j + 1],
                        arr[i + 2][j], arr[i + 2][j + 1], arr[i + 2][j + 2]]
            print(elements)
            response.append(sum(elements))
    return max(response)
