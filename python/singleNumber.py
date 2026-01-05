# https://leetcode.com/problems/single-number/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        single = 0
        for num in nums:
            single ^= num  # XOR all numbers
        return single
