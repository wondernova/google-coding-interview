def test_product_of_array_except_self():
    """
    integer로 구성된 array가 주어지며, 모든 값은 1보다 크다.
    이때 자기 자신을 제외한 다른 elements들의 곱을 계산한 array를 리턴한다

    제약사항
     - division 사용하지 말것
     - O(n) 으로 문제 해결

    Input: [1, 2, 3, 4]
    Output: [24, 12, 8, 6]

     - 24: 2 * 3 * 4
     - 12: 1 * 3 * 4
     - 8 : 1 * 2 * 4
     - 6 : 1 * 2 * 3

    """

    # 최적화된 방법
    assert my_code([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert my_code([3, 1, 1, 4]) == [4, 12, 12, 3]
    assert my_code([2, 4, 1, 5, 3]) == [60, 30, 120, 24, 40]

    # division을 사용해서 문제를 푼다
    assert division_solution([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert division_solution([3, 1, 1, 4]) == [4, 12, 12, 3]
    assert division_solution([2, 4, 1, 5, 3]) == [60, 30, 120, 24, 40]


def my_code(arr):
    """
    array : [ 2,  4,   1,  5,  3]
    left  : [ 1,  2,   8,  8, 40] <- 앞에 1을 놓고 array와 계속 곱한다
    right : [60, 15,  15,  3,  1] <- 맨끝에 1을 놓고 array에 계속 곱한다
    answer: [60, 30, 120, 24, 40] <- left * right

    즉.... 1이라는 것이
    array : [  a,   b,   c,   d]
    left  : [  1,   a,  ab, abc]
    right : [bcd,  cd,   d,   1]
    answer: [bcd, acd, abd, abc]
    """
    n = len(arr)
    ans = [1] * n
    for i in range(1, n):
        ans[i] = ans[i - 1] * arr[i - 1]

    right = 1
    for i in range(n - 1, 0, -1):
        right *= arr[i]
        ans[i - 1] *= right
    return ans


def division_solution(arr):
    """
    모든 값을 먼저 곱한후, 해당 element로 나눠준다

    1 * 2 * 3 * 4 = 24
    [24/1, 24/2, 24/3, 24/6]
    """

    total_prod = 1
    for v in arr:
        total_prod *= v

    answer = []
    for v in arr:
        answer.append(int(total_prod / v))

    return answer
