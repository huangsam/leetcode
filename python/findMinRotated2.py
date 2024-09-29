# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[h]:
                l = m + 1
            elif nums[m] < nums[h]:
                h = m
            else:
                h = h - 1
        return nums[l]
