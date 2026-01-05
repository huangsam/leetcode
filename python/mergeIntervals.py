# https://leetcode.com/problems/merge-intervals/

from typing import List, Optional


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals.
        
        Complexity:
        - Time: O(n * log(n))
        - Space: O(n)
        """
        # Sort by start time, and then sort by end time
        intervals.sort()

        # Assume that there is at least one interval
        result = [intervals[0]]

        for curr_interval in intervals[1:]:
            prev_interval = result[-1]
            new_interval = self._newInterval(prev_interval, curr_interval)

            # For overlap use case
            if new_interval is not None:
                result[-1] = new_interval

            # For non-overlap use case
            else:
                result.append(curr_interval)

        return result

    def _newInterval(self, first, second) -> Optional[List[int]]:
        start_1, end_1 = first
        start_2, end_2 = second

        # First partially overlaps second
        if start_2 <= end_1 <= end_2:
            return [start_1, end_2]

        # First fully overlaps second
        elif end_1 > end_2:
            return [start_1, end_1]

        # We do not need to check the inverse since the original
        # interval list is fully sorted, so we know for sure that
        # start_1 <= start_2
        return None
