# https://leetcode.com/problems/total-hamming-distance/
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for i in range(32):
            mask = 1 << i
            countOnes = 0
            countZeros = 0
            for num in nums:
                if num & mask != 0:
                    countOnes += 1
                else:
                    countZeros += 1
            count += countOnes * countZeros
        return count
