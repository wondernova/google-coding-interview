def test_find_median_from_data_stream():
    """
    https://leetcode.com/problems/find-median-from-data-stream/
    """

    # Test 1
    med_finder = MedianFinder()
    med_finder.addNum(4)
    assert med_finder.findMedian() == 4
    med_finder.addNum(3)
    assert med_finder.findMedian() == 3.5
    med_finder.addNum(1)
    assert med_finder.findMedian() == 3
    med_finder.addNum(-1)
    assert med_finder.findMedian() == 2
    med_finder.addNum(-5)
    assert med_finder.findMedian() == 1
    med_finder.addNum(100)
    assert med_finder.findMedian() == 2
    med_finder.addNum(200)
    assert med_finder.findMedian() == 3


import heapq as hq


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            hq.heappush(self.large, -hq.heappushpop(self.small, -num))
        else:
            hq.heappush(self.small, -hq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        return self.large[0]
