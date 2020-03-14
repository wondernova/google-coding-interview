def test_elevator_stop():
    """
    Codility Elevator Stop 문제

    - m : floors
    - x : maximum people
    - Y: 엘리베이터가 한번에 태울수 있는 총중량
    - A: list of the weight of each person
    - B: 몇층에서 내리는지
    """

    # Test 1
    #  1층에서 60, 80 옮기고 (3) -> 다시 1층와서 (1) -> 40 옮긴다 (1) = 총 5번
    weights = [60, 80, 40]  # A
    destinations = [2, 3, 5]  # B
    max_floor = 5  # M
    max_people = 2  # X
    max_weight = 200  # Y
    assert solution(weights, destinations, max_floor, max_people, max_weight) == 5

    # Test 2
    weights = [60, 80, 40]  # A
    destinations = [2, 3, 5]  # B
    max_floor = 5  # M
    max_people = 4  # X
    max_weight = 100  # Y
    assert solution(weights, destinations, max_floor, max_people, max_weight) == 6

    # Test 3
    # 1층 (1) -> 다태우고 2층 (1)
    weights = [20, 20, 100, 50, 10, 100]  # A
    destinations = [2, 2, 2, 2, 2, 2]  # B
    max_floor = 6  # M
    max_people = 6  # X
    max_weight = 500  # Y
    assert solution(weights, destinations, max_floor, max_people, max_weight) == 2

    # Test 4
    weights = [20, 20, 50, 50, 10, 100, 60, 60]  # A
    destinations = [2, 3, 2, 4, 5, 5, 3, 2]  # B
    max_floor = 6  # M
    max_people = 6  # X
    max_weight = 200  # Y
    assert solution(weights, destinations, max_floor, max_people, max_weight) == 10


def solution(weights, destinations, max_floor, max_people, max_weight):
    n = len(weights)
    n_stop = i = 0

    while i < n:
        cur_weight = 0
        cur_people = 0
        uniq_floors = set()

        while i < n and cur_people < max_people and cur_weight + weights[i] <= max_weight:
            uniq_floors.add(destinations[i])
            cur_weight += weights[i]
            cur_people += 1
            i += 1
        n_stop += len(uniq_floors) + 1
    return n_stop
