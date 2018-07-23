def test_find_the_running_median():
    """
    먼저 median값을 찾기 위해서는 dataset을 ascending sort를 해야 합니다. 
    
    이후 만약 데이터가 odd number라면 중앙값이 median이 됩니다.
    예를 들어 {1, 2, 3} 에서 median 값은 2 입닏.ㅏ
    
    만약 데이터가 even number 라면 두개의 중앙값의 평균값이 median이 됩니다.
    예를 들어 {1, 2, 3, 4} 라면 (2+3)/2 = 2.5 가 median값이 됩니다.

    median 값 찾는 함수를 만드세요
    """

    data = [12, 4, 5, 3, 8, 7]

    for i in range(len(data)):
        find_median(data[:i + 1])

def find_median(data):
