# https://leetcode.com/problems/total-hamming-distance/

from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        Calculate the total Hamming distance between all pairs of integers.
        
        Complexity:
        - Time: O(n)
        - Space: O(1)

        Calculate the total Hamming distance between all pairs of integers in the list.
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
