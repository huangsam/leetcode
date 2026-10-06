# https://leetcode.com/problems/find-median-from-data-stream/

import heapq


class MedianFinder:
    """
    Data structure that supports adding numbers from a data stream and finding
    the median in real-time.

    Approach:
    - Use two heaps to divide the numbers into two equal (or almost equal) halves:
      1. small: A max-heap storing the smaller half of numbers (inverted values using heapq).
      2. large: A min-heap storing the larger half of numbers.
    - Invariants:
      1. Every value in small <= every value in large.
      2. len(small) == len(large) or len(small) == len(large) + 1.
    - On addNum(num):
      - Push num into small (as -num).
      - Pop largest from small and push into large (preserves ordering invariant).
      - If large has more elements than small, pop smallest from large and push back into small.
    - On findMedian():
      - If small has more elements, median is the top of small (-small[0]).
      - If heaps are balanced in size, median is the average of tops of small and large.

    Complexity:
    - Time:
        - addNum: O(log n) to insert and rebalance heaps
        - findMedian: O(1) to inspect heap roots
    - Space: O(n) where n is the number of elements added
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
