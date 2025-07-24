# https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        xor_result = x ^ y

        while xor_result > 0:
            xor_result, remainder = divmod(xor_result, 2)
            distance += remainder

        return distance
