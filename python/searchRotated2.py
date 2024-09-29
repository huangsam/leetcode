# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, h = 0, len(nums) - 1
        while l <= h:
            while l < h and nums[l] == nums[l + 1]:
                l += 1
            while h > l and nums[h] == nums[h - 1]:
                h -= 1
            m = (l + h) // 2
            if target == nums[m]:
                return True
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            elif nums[m] <= target <= nums[h]:
                l = m + 1
            else:
                h = m - 1
        return False
