# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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
