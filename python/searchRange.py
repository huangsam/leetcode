# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found = self.binarySearch(nums, target, 0, len(nums) - 1)
        if found == -1:
            return [-1, -1]
        left, right = found, found
        while True:
            result = self.binarySearch(nums, target, 0, left - 1)
            if result == -1:
                break
            left = result
        while True:
            result = self.binarySearch(nums, target, right + 1, len(nums) - 1)
            if result == -1:
                break
            right = result
        return [left, right]

    def binarySearch(self, nums: List[int], target: int, lo: int, hi: int):
        found = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                found = mid
                break
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return found
