# https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        xor_result = bin(x ^ y)[2:]
        for bit in xor_result:
            if bit == "1":
                distance += 1
        return distance
