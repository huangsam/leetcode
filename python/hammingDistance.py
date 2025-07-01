# https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0

        # Calculate the XOR of x and y
        xor_result = x ^ y

        # Count the number of '1's in the binary output
        while xor_result > 0:
            if xor_result & 1:
                distance += 1
            xor_result >>= 1

        return distance
