# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, h = 0, len(nums)-1
        while l <= h:
            m = (l + h) // 2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    l, h = l, m-1
                else:
                    l, h = m+1, h
            elif nums[m] <= target <= nums[h]:
                l, h = m+1, h
            else:
                l, h = l, m-1
        return -1
