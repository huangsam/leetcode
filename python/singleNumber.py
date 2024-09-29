# https://leetcode.com/problems/single-number/
from typing import List


class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single
