# https://leetcode.com/problems/total-hamming-distance/

from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        Calculate the total Hamming distance between all pairs of integers.

        The Hamming distance between two numbers is the number of positions where
        their bits differ. To compute the total for all pairs efficiently, for each
        bit position, count the number of numbers with 1 and with 0. The contribution
        to the total distance for that bit is (count1 * count0), as each pair with
        different bits adds 1. Sum over all 32 bits.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        count = 0
        for i in range(32):  # Check each bit position
            mask = 1 << i
            countOnes = 0
            countZeros = 0
            for num in nums:
                if num & mask != 0:
                    countOnes += 1
                else:
                    countZeros += 1
            count += countOnes * countZeros  # Pairs with different bits
        return count
