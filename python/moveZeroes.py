# https://leetcode.com/problems/move-zeroes/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        non_zero_found = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_found] = nums[non_zero_found], nums[i]
                non_zero_found += 1
