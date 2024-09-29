# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        m = (l + h) // 2
        if len(nums) <= 2:
            return min(nums)
        mid = nums[m]
        last = nums[h]
        if mid > last:
            return self.findMin(nums[m : h + 1])
        return self.findMin(nums[l : m + 1])

    def findMinIterative(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while h - l > 2:
            m = (l + h) // 2
            mid = nums[m]
            last = nums[h]
            if mid > last:
                l = m
            else:
                h = m
        return min(nums[l : h + 1])
