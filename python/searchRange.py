# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Find the starting and ending position of a target value.

        Perform two binary searches: one to find the leftmost index where nums[i] >= target,
        another for the rightmost where nums[i] <= target.

        If the range is valid and nums[left] == target, return [left, right], else [-1, -1].

        Complexity:
        - Time: O(log(n))
        - Space: O(1)
        """
        if not nums:
            return [-1, -1]

        left = self._findBoundary(nums, target, True)
        if left == -1:
            return [-1, -1]

        right = self._findBoundary(nums, target, False)
        return [left, right]

    def _findBoundary(self, nums: List[int], target: int, find_left: bool) -> int:
        """Binary search to find leftmost or rightmost occurrence."""
        lo, hi = 0, len(nums) - 1
        result = -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                result = mid
                # Continue searching in the appropriate direction
                if find_left:
                    hi = mid - 1  # Search left for first occurrence
                else:
                    lo = mid + 1  # Search right for last occurrence
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return result
