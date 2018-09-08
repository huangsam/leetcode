# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, h = 0, len(nums)-1
        while l <= h:
            while l < h and nums[l] == nums[l + 1]:
                l += 1
            while h > l and nums[h] == nums[h - 1]:
                h -= 1
            m = (l + h) // 2
            if target == nums[m]:
                return True
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    l, h = l, m-1
                else:
                    l, h = m+1, h
            elif target >= nums[m] and target <= nums[h]:
                l, h = m+1, h
            else:
                l, h = l, m-1
        return False
