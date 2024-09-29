# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] <= target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
