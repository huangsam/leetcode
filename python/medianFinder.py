# https://leetcode.com/problems/find-median-from-data-stream/

import heapq


class MedianFinder:
    """
    Data structure that supports adding numbers from a data stream and finding
    the median in real-time.

    Approach:
    - Divide incoming numbers between a max-heap (small half) and a min-heap (large half)
    - Invariant 1: every value in small <= every value in large
    - Invariant 2: small heap size is equal to or exactly one greater than large heap size
    - On addNum: push to small heap, move largest to large heap, then balance sizes
    - On findMedian: return top of small heap if odd, or average of tops if even

    Complexity:
    - Time: O(log n) for addNum, O(1) for findMedian
    - Space: O(n) where n is total numbers added
    """

    def __init__(self):
        # Max-heap for the smaller half (store negated values)
        self.small: list[int] = []
        # Min-heap for the larger half
        self.large: list[int] = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        # Balance value: highest of small must go to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance size: small can have at most 1 more element than large
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
