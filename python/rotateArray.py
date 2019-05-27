# https://leetcode.com/problems/rotate-array/
class Solution(object):
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)
        k = k % nlen
        self.reverse(nums, 0, nlen - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, nlen - 1)
