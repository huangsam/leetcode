# https://leetcode.com/problems/single-number/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Find the element that appears only once in an array.

        XOR all numbers: pairs of identical numbers XOR to 0, and 0 XOR single
        number = single number.

        This works because XOR is associative, commutative, and a ^ a = 0, 0 ^ b = b.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        single = 0
        for num in nums:
            single ^= num  # XOR all numbers
        return single
