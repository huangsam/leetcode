# https://leetcode.com/problems/single-number-ii/
from typing import List


class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        num_to_freq = {}
        for num in nums:
            if num in num_to_freq:
                num_to_freq[num] += 1
            else:
                num_to_freq[num] = 1
        for num, freq in num_to_freq.items():
            if freq == 1:
                return num
