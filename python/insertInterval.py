# https://leetcode.com/problems/insert-interval/

from collections import deque
from typing import Deque, List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Here are a few cases that we can consider for newInterval:

        Case 1: newInterval does not overlap with any interval
        Case 2: newInterval overlaps with one interval
        Case 3: newInterval overlaps with multiple intervals

        Case 1: If we find a case that newInterval is in between
        previous and current, then we can pump in newInterval
        followed by current.

        Case 2 + 3: Upon finding the first overlap, we collect all
        overlaps and merge them together with newInterval. This
        final merged overlap is gauranteed to not overlap with
        any other interval which brings us back to Case 1.
        """
        if len(intervals) == 0:
            return [newInterval]

        cleans: List[List[int]] = []
        overlaps: List[List[int]] = []
        for interval in intervals:
            first, second = self.sort_swap(interval, newInterval)
            if self.has_overlap(first, second):
                overlaps.append(interval)
            else:
                cleans.append(interval)

        overlaps.append(newInterval)
        merged_overlap: List[int] = overlaps[0]
        for overlap in overlaps[1:]:
            merged_overlap = self.merge(merged_overlap, overlap)

        if len(cleans) == 0:
            return [merged_overlap]

        if len(cleans) == 1:
            return self.sort_swap(cleans[0], merged_overlap)

        result: Deque[List[int]] = deque()
        result_has_overlap: bool = False
        for clean in cleans:
            if len(result) > 0 and self.is_between(result[-1], merged_overlap, clean):
                result.append(merged_overlap)
                result.append(clean)
                result_has_overlap = True
            else:
                result.append(clean)

        if result_has_overlap is False:
            if merged_overlap < result[0]:
                result.appendleft(merged_overlap)
            else:
                result.append(merged_overlap)

        return list(result)

    def has_overlap(self, first: List[int], second: List[int]) -> bool:
        """
        Some cases to consider:

        1->5, 5->8 (touching overlap)
        1->10, 5->8 (full overlap)
        5->9, 5->8 (overflow overlap)
        5->8, 5->8 (exact overlap)
        """
        return first[0] <= second[0] and first[1] >= second[0]

    def merge(self, first: List[int], second: List[int]) -> List[int]:
        return [min(first[0], second[0]), max(first[1], second[1])]

    def sort_swap(self, first: List[int], second: List[int]) -> List[List[int]]:
        return [first, second] if first < second else [second, first]

    def is_between(self, first: List[int], second: List[int], third: List[int]) -> bool:
        return all([first[0] <= second[0] <= third[0], not self.has_overlap(first, second), not self.has_overlap(second, third)])
