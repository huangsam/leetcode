# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        mid = (lo + hi) // 2
        if len(nums) <= 2:
            return min(nums)
        mid_val = nums[mid]
        last_val = nums[hi]
        if mid_val > last_val:
            return self.findMin(nums[mid : hi + 1])
        return self.findMin(nums[lo : mid + 1])

    def findMinIterative(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while hi - lo > 2:
            mid = (lo + hi) // 2
            mid_val = nums[mid]
            last_val = nums[hi]
            if mid_val > last_val:
                lo = mid
            else:
                hi = mid
        return min(nums[lo : hi + 1])
