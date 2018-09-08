# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums)-1
        m = (l + h) // 2
        if len(nums) <= 2:
            return min(nums)
        mid = nums[m]
        last = nums[h]
        if mid > last:
            return self.findMin(nums[m:h+1])
        return self.findMin(nums[l:m+1])

    def findMinIterative(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums)-1
        while h - l > 2:
            m = (l + h) // 2
            mid = nums[m]
            last = nums[h]
            if mid > last:
                l, h = m, h
            else:
                l, h = l, m
        return min(nums[l:h+1])
