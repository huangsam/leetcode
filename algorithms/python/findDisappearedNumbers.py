# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        n_len = len(nums)
        for i in range(n_len):
            num = abs(nums[i])
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
        n_len = len(nums)
        for i in range(n_len):
            if nums[i] > 0:
                result.append(i + 1)
        return result
