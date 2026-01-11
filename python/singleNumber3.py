# https://leetcode.com/problems/single-number-iii/

from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Find two elements that appear only once when others appear twice.

        Since all elements except two appear exactly twice, we can use a frequency
        map to count occurrences. The elements with count 1 are the ones that appear
        only once. Alternatively, using XOR: XOR all numbers to get XOR of the two
        singles. Find a set bit in that XOR, divide numbers into two groups based
        on that bit, and XOR each group to find the two numbers.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        mapping: DefaultDict[int, int] = defaultdict(int)
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
