# https://leetcode.com/problems/single-number-iii/

from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(1)
        """        mapping: DefaultDict[int, int] = defaultdict(int)
        for num in nums:
            mapping[num] += 1
        result = []
        for k, v in mapping.items():
            if v == 1:
                result.append(k)
        return result

    def singleNumberBits(self, nums: List[int]) -> List[int]:
        left = 0
        right = 0
        xor = 0
        for num in nums:
            xor ^= num

        # Find rightmost set bit since left and right are different
        set_bit = xor & ~(xor - 1)

        # Run xor based on set bit
        for num in nums:
            if num & set_bit != 0:
                left ^= num
            else:
                right ^= num
        return [left, right]
