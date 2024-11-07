# https://leetcode.com/problems/insert-interval/

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        # Insert newInterval at start or middle, if possible
        pointer = 0
        while pointer < len(intervals):
            if newInterval[0] <= intervals[pointer][0]:
                intervals.insert(pointer, newInterval)
                break
            pointer += 1

        # Insert newInterval at end, if needed
        if pointer == len(intervals) and newInterval != intervals[-1]:
            intervals.insert(pointer, newInterval)

        # Merge any and all relevant intervals
        new_intervals = [intervals[0]]
        for interval in intervals[1:]:
            if self.isOverlap(new_intervals[-1], interval):
                new_intervals[-1] = self.mergeTwo(new_intervals[-1], interval)
            else:
                new_intervals.append(interval)

        return new_intervals

    def isOverlap(self, i1: List[int], i2: List[int]) -> bool:
        return i1[0] <= i2[0] and i1[1] >= i2[0]

    def mergeTwo(self, i1: List[int], i2: List[int]) -> List[int]:
        return [min(i1[0], i2[0]), max(i1[1], i2[1])]
