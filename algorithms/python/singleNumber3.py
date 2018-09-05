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

    def singleNumberBits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = 0
        xor = 0
        for num in nums:
            xor ^= num

        # find rightmost set bit
        # since left and right are different
        set_bit = xor & ~(xor - 1)

        # run xor based on set bit
        for num in nums:
            if num & set_bit != 0:
                left ^= num
            else:
                right ^= num
        return (left, right)
