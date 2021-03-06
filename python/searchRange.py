# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
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

    def binarySearch(self, nums, target, lo, hi):
        found = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                found = mid
                break
            elif nums[mid] < target:
                lo, hi = mid + 1, hi
            else:
                lo, hi = lo, mid - 1
        return found
