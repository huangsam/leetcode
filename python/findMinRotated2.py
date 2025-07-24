# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1  # Minimum is in the right half
            elif nums[mid] < nums[hi]:
                hi = mid  # Minimum is in the left half including mid
            else:
                hi = hi - 1  # Cannot determine, reduce search space
        return nums[lo]
