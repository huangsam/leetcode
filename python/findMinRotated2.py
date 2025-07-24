# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi = hi - 1
        return nums[lo]
