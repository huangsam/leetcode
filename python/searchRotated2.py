# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            while lo < hi and nums[lo] == nums[lo + 1]:
                lo += 1
            while hi > lo and nums[hi] == nums[hi - 1]:
                hi -= 1
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return True
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] <= target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
