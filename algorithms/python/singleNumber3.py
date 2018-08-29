# https://leetcode.com/problems/single-number-iii/description/
from collections import defaultdict


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1
        result = []
        for k, v in mapping.items():
            if v == 1:
                result.append(k)
        return result
