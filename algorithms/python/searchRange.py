# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution:
    def binarySearch(self, nums, target, lo, hi):
        found = -1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                found = mid
                break
            elif nums[mid] < target:
                lo, hi = mid + 1, hi
            else:
                lo, hi = lo, mid
        return found
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, h = 0, len(nums)
        found = self.binarySearch(nums, target, 0, len(nums))
        if found == -1:
            return [-1, -1]
        left, right = found, found
        while True:
            result = self.binarySearch(nums, target, 0, left)
            if result == -1 or result == found or result == left:
                break
            left = result
        while True:
            result = self.binarySearch(nums, target, right, len(nums))
            if result == -1 or result == found or result == right:
                break
            right = result
        return [left, right]
