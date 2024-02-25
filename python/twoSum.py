# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, ival in nums.items():
            num_map[ival] = i
            complement = target - ival
            if num_map.get(complement):
                return [ival, complement]
        return [-1, -1]
