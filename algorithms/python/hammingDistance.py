# https://leetcode.com/problems/hamming-distance/
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        xor_result = bin(x ^ y)[2:]
        for bit in xor_result:
            if bit == '1':
                distance += 1
        return distance
