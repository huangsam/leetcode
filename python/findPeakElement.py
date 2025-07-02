# https://leetcode.com/problems/find-peak-element/

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            # Avoid mid overflow by using the formula below
            mid = lo + (hi - lo) // 2

            if nums[mid] < nums[mid + 1]:
                # If nums[mid] is less than the element to its right,
                # then a peak must exist to the right of mid
                lo = mid + 1
            else:
                # Otherwise (nums[mid] >= nums[mid+1]),
                # a peak could be mid itself, or to the left of mid
                hi = mid

        # lo == hi and this index points to a peak element
        return lo
