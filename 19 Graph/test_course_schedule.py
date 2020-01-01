def test_course_schedule():
    """
    https://leetcode.com/problems/course-schedule/

    There are a total of n courses you have to take, labeled from 0 to n-1.
    Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
    Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

    [Example 1]
    Input: 2, [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
                 To take course 1 you should have finished course 0. So it is possible.


    [Example 2]
    Input: 2, [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
                 To take course 1 you should have finished course 0, and to take course 0 you should
                 also have finished course 1. So it is impossible.

    기본적으로 Cycle이 있는지 없는지 체크하면 되고, graph문제임.
    """

    assert check_course_schedule([[1, 0]])
    assert not check_course_schedule([[1, 0], [0, 1]])
    assert check_course_schedule([[4, 3], [3, 1], [3, 2], [2, 0], [1, 0]])
    assert not check_course_schedule([[0, 4], [4, 3], [3, 1], [3, 2], [2, 0], [1, 0]])
    assert check_course_schedule([[3, 1], [2, 1], [1, 0], [6, 5], [5, 4]])


def check_course_schedule(courses):
    graph = dict()  # {course: [prerequisites...]}
    for edge in courses:
        graph.setdefault(edge[0], [])
        graph[edge[0]].append(edge[1])

    visited = set()

    def is_visited(vertex):
        if vertex in graph:
            visited.add(vertex)
            for prerequisite in graph[vertex]:
                if prerequisite in visited or is_visited(prerequisite):
                    return True
            visited.remove(vertex)
        return False

    for vertex in graph:
        if is_visited(vertex):
            return False
    return True
